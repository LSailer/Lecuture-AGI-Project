from typing import Any

from dotenv import load_dotenv
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
            do_sample=True,
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
            do_sample=True,
            temperature=temperature,
        )
        return [r[0]["generated_text"] for r in results]


if __name__ == "__main__":
    mps_device = "mps" if torch.backends.mps.is_available() else "cpu"
    llm_instance = LLM(device=mps_device)
    system_prompt = "You are a helpful assistant."
    prompt = "What is the capital of France?"
    response = llm_instance.generate(system_prompt, prompt)
    print(response)
