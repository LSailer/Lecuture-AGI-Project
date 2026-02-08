"""Fallback model for prompt rewriting when all agents fail a step."""

import asyncio
import os
import re
from typing import Any

from google import genai

# Type for a single failed prediction record
FailedPrediction = dict[str, str]


class FallbackModel:
    """Calls a fallback model to rewrite system/user prompts when all agents fail."""

    def __init__(self, config: dict[str, Any], device: str = "cpu") -> None:
        self.max_retries: int = config.get("max_fallback_retries", 3)
        self.fallback_api: str = config.get("fallback_api", "gemini")
        self.gemini_model: str = config.get("gemini_model", "gemini-2.5-flash")
        self.local_model_id: str = config.get(
            "fallback_local_model", "deepseek-ai/DeepSeek-R1-Distill-Qwen-32B"
        )
        self.device = device
        self._local_pipe: Any = None  # Lazy-loaded

    def _build_meta_prompt(
        self,
        system_prompt: str,
        user_prompt: str,
        failed_predictions: list[FailedPrediction],
    ) -> str:
        """Build a meta-prompt asking the fallback to improve the prompts."""
        failures_text = "\n".join(
            f"  - Agent {fp['agent_id']}: predicted action={fp['action']}, "
            f"predicted state={fp['state']}, error={fp['error']}"
            for fp in failed_predictions
        )
        return f"""You are a prompt-engineering expert. A multi-agent voting system is trying to solve
a puzzle. All agents failed on the current step. Your job is to analyze the failures
and produce improved system and user prompts that will help the agents reason better.

## Original System Prompt
{system_prompt}

## Original User Prompt
{user_prompt}

## Failed Predictions
{failures_text}

## Instructions
1. Analyze why the agents failed (wrong parsing, bad reasoning, invalid moves, etc.).
2. Produce an improved system prompt and user prompt that address the failure modes.
3. Keep the same output format requirements (move = [...], next_state = [...]).
4. You CAN and SHOULD use the placeholders `{{current_state}}`, `{{previous_move}}`, and `{{state_visual}}` (if applicable) in your improved user prompt. Do NOT hardcode the state from the failed step.
5. Output your response in EXACTLY this format:

<SYSTEM_PROMPT>
(your improved system prompt here)
</SYSTEM_PROMPT>

<USER_PROMPT>
(your improved user prompt here)
</USER_PROMPT>
"""

    def update_compose(
        self,
        system_prompt: str,
        user_prompt: str,
        failed_predictions: list[FailedPrediction],
        step: int = 0,
        retry: int = 0,
    ) -> tuple[str, str]:
        """Returns (new_system_prompt, new_user_prompt) by calling fallback model."""
        meta_prompt = self._build_meta_prompt(
            system_prompt, user_prompt, failed_predictions
        )

        response: str | None = None
        if self.fallback_api in ("gemini", "both"):
            try:
                response = self._call_gemini(meta_prompt)
            except Exception as e:
                print(f"Gemini API failed: {e}")

        if response is None and self.fallback_api in ("local", "both"):
            try:
                response = self._call_local(meta_prompt)
            except Exception as e:
                print(f"Local fallback model failed: {e}")

        if response is None:
            print("All fallback models failed, returning original prompts.")
            return system_prompt, user_prompt

        new_system, new_user = self._parse_response(
            response, system_prompt, user_prompt
        )

        # Debug prompt tracking
        self._log_debug_prompts(step, retry, new_system, new_user, failed_predictions)

        return new_system, new_user

    def _call_gemini(self, meta_prompt: str) -> str:
        """Call Gemini API synchronously (wraps async internally)."""
        api_key = os.environ.get("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY environment variable not set")

        try:
            loop = asyncio.get_running_loop()
        except RuntimeError:
            loop = None

        if loop and loop.is_running():
            # Already in an async context — run in a new thread
            import concurrent.futures

            with concurrent.futures.ThreadPoolExecutor() as pool:
                result = pool.submit(
                    asyncio.run, self._call_gemini_async(meta_prompt)
                ).result()
            return result
        else:
            return asyncio.run(self._call_gemini_async(meta_prompt))

    async def _call_gemini_async(self, meta_prompt: str) -> str:
        """Async Gemini API call using google-genai SDK."""
        api_key = os.environ.get("GEMINI_API_KEY")
        client = genai.Client(api_key=api_key)
        response = await client.aio.models.generate_content(
            model=self.gemini_model,
            contents=meta_prompt,
        )
        return response.text

    def _call_local(self, meta_prompt: str) -> str:
        """Lazy-load and call the local DeepSeek fallback model."""
        if self._local_pipe is None:
            print(f"Loading local fallback model: {self.local_model_id}")
            from transformers import pipeline

            if self.device == "cuda":
                self._local_pipe = pipeline(
                    "text-generation",
                    model=self.local_model_id,
                    device_map=self.device,
                )
            else:
                self._local_pipe = pipeline(
                    "text-generation",
                    model=self.local_model_id,
                    device=self.device,
                )

        messages: list[dict[str, str]] = [
            {"role": "system", "content": "You are a prompt-engineering expert."},
            {"role": "user", "content": meta_prompt},
        ]
        result: Any = self._local_pipe(messages, max_new_tokens=1500, do_sample=False)
        return result[0]["generated_text"][-1]["content"]

    def _parse_response(
        self, response: str, default_system: str, default_user: str
    ) -> tuple[str, str]:
        """Parse the fallback model's response to extract new prompts."""
        sys_match = re.search(
            r"<SYSTEM_PROMPT>\s*(.*?)\s*</SYSTEM_PROMPT>", response, re.DOTALL
        )
        usr_match = re.search(
            r"<USER_PROMPT>\s*(.*?)\s*</USER_PROMPT>", response, re.DOTALL
        )

        new_system = sys_match.group(1).strip() if sys_match else default_system
        new_user = usr_match.group(1).strip() if usr_match else default_user

        return new_system, new_user

    def _log_debug_prompts(
        self,
        step: int,
        retry: int,
        system_prompt: str,
        user_prompt: str,
        failed_predictions: list[FailedPrediction],
    ) -> None:
        """Append debug info to output/debug_prompts.md."""
        os.makedirs("output", exist_ok=True)
        debug_path = os.path.join("output", "debug_prompts.md")

        failures_text = "\n".join(
            f"- Agent {fp['agent_id']}: action={fp['action']}, "
            f"state={fp['state']}, error={fp['error']}"
            for fp in failed_predictions
        )

        with open(debug_path, "a") as f:
            f.write(f"\n## Fallback at Step {step}, Retry {retry}\n\n")
            f.write(f"### System Prompt\n{system_prompt}\n\n")
            f.write(f"### User Prompt\n{user_prompt}\n\n")
            f.write(f"### Failed Predictions\n{failures_text}\n\n")
            f.write("---\n")
