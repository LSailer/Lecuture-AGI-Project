from dotenv import load_dotenv
import torch
from transformers import pipeline

load_dotenv()


class LLM:
    def __init__(self, model_id="LLM/model", device="cpu") -> None:
        print(f"LLM initialized with model {model_id} on device {device}")
        if device == "cpu":
            self.pipe = pipeline("text-generation", model=model_id, device=device)
        else:
            self.pipe = pipeline("text-generation", model=model_id, device_map=device)

    def generate(
        self,
        system_prompt: str,
        user_prompt: str,
        max_new_tokens: int = 750,
        temperature: float = 0.1,
    ) -> str:
        message = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ]
        result = self.pipe(
            message,
            max_new_tokens=max_new_tokens,
            do_sample=False,
            temperature=temperature,
        )
        return result[0]["generated_text"]  # type: ignore #ignore


if __name__ == "__main__":
    mps_device = "mps" if torch.backends.mps.is_available() else "cpu"
    llm_instance = LLM(device=mps_device)
    system_prompt = "You are a helpful assistant."
    prompt = "What is the capital of France?"
    response = llm_instance.generate(system_prompt, prompt)
    print(response)
