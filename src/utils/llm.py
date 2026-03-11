from typing import Any

from dotenv import load_dotenv
import torch
from transformers import pipeline

try:
    import weave
except ImportError:
    class _WeaveStub:
        @staticmethod
        def op():
            def decorator(fn):
                return fn
            return decorator

        @staticmethod
        def init(*args, **kwargs):
            return None

    weave = _WeaveStub()


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

    @weave.op()
    def generate(
        self,
        system_prompt: str,
        user_prompt: str,
        max_new_tokens: int = 750,
        temperature: float = 0.5,
        do_sample: bool = False,
        top_p: float = 1.0,
    ) -> list[Message]:
        message: Conversation = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ]
        gen_kwargs: dict[str, Any] = {
            "max_new_tokens": max_new_tokens,
            "do_sample": do_sample,
        }
        if do_sample:
            gen_kwargs["temperature"] = temperature
            gen_kwargs["top_p"] = top_p

        result: Any = self.pipe(message, **gen_kwargs)
        return result[0]["generated_text"]

    @weave.op()
    def generate_batch(
        self,
        messages_list: list[Conversation],
        max_new_tokens: int = 750,
        temperature: float = 0.5,
        do_sample: bool = False,
        top_p: float = 1.0,
    ) -> list[list[Message]]:
        """Run multiple prompts through the model in a single batch."""
        gen_kwargs: dict[str, Any] = {
            "batch_size": len(messages_list),
            "max_new_tokens": max_new_tokens,
            "do_sample": do_sample,
        }
        if do_sample:
            gen_kwargs["temperature"] = temperature
            gen_kwargs["top_p"] = top_p

        results: Any = self.pipe(messages_list, **gen_kwargs)
        return [r[0]["generated_text"] for r in results]


if __name__ == "__main__":
    mps_device = "mps" if torch.backends.mps.is_available() else "cpu"
    llm_instance = LLM(device=mps_device)
    system_prompt = "You are a helpful assistant."
    prompt = "What is the capital of France?"
    response = llm_instance.generate(system_prompt, prompt, do_sample=False)
    print(response)