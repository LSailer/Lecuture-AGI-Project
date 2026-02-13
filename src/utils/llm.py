import asyncio
from typing import Any

from dotenv import load_dotenv
import ollama
import torch
from transformers import pipeline


load_dotenv()

# Type alias for chat messages: [{"role": "...", "content": "..."}]
Message = dict[str, str]
Conversation = list[Message]


class LLM:
    def __init__(self, model_id: str = "LLM/model", device: str = "cpu") -> None:
        print(f"LLM initialized with model {model_id} on device {device}")

        if device == "cuda":
            self.pipe = pipeline("text-generation", model=model_id, device_map=device)

        else:
            self.pipe = pipeline("text-generation", model=model_id, device=device)

    def generate(
        self,
        system_prompt: str,
        user_prompt: str,
        max_new_tokens: int = 750,
        temperature: float = 0.5,
    ) -> list[Message]:
        message: Conversation = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ]
        result: Any = self.pipe(
            message,
            max_new_tokens=max_new_tokens,
            do_sample=False,
            temperature=temperature,
        )
        return result[0]["generated_text"]

    def generate_batch(
        self,
        messages_list: list[Conversation],
        max_new_tokens: int = 750,
        temperature: float = 0.5,
    ) -> list[list[Message]]:
        """Run multiple prompts through the model in a single batch."""
        results: Any = self.pipe(
            messages_list,
            batch_size=len(messages_list),
            max_new_tokens=max_new_tokens,
            do_sample=False,
            temperature=temperature,
        )
        return [r[0]["generated_text"] for r in results]


class OllamaLLM:
    def __init__(self, model_id: str = "qwen3:8b") -> None:
        self.model_id = model_id
        print(f"OllamaLLM initialized with model {model_id}")

    def generate(
        self,
        system_prompt: str,
        user_prompt: str,
        max_new_tokens: int = 750,
        temperature: float = 0.5,
    ) -> list[Message]:
        messages: Conversation = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ]
        response = ollama.chat(
            model=self.model_id,
            messages=messages,
            options={"num_predict": max_new_tokens, "temperature": temperature},
        )
        return messages + [{"role": "assistant", "content": response.message.content}]

    def generate_batch(
        self,
        messages_list: list[Conversation],
        max_new_tokens: int = 750,
        temperature: float = 0.5,
    ) -> list[list[Message]]:
        async def _run_all() -> list[list[Message]]:
            client = ollama.AsyncClient()

            async def _single(messages: Conversation) -> list[Message]:
                response = await client.chat(
                    model=self.model_id,
                    messages=messages,
                    options={"num_predict": max_new_tokens, "temperature": temperature},
                )
                return messages + [{"role": "assistant", "content": response.message.content}]

            return list(await asyncio.gather(*[_single(m) for m in messages_list]))

        return asyncio.run(_run_all())


def create_llm(config: dict, device: str) -> "LLM | OllamaLLM":
    backend = config.get("llm_backend", "huggingface")
    if backend == "ollama":
        return OllamaLLM(model_id=config.get("ollama_model", "qwen3:8b"))
    return LLM(model_id=config.get("model_id", "LLM/model"), device=device)


if __name__ == "__main__":
    mps_device = "mps" if torch.backends.mps.is_available() else "cpu"
    llm_instance = LLM(device=mps_device)
    system_prompt = "You are a helpful assistant."
    prompt = "What is the capital of France?"
    response = llm_instance.generate(system_prompt, prompt)
    print(response)
