from dotenv import load_dotenv
from huggingface_hub import snapshot_download

load_dotenv()

MODELS = {
    "qwen3-32b": "Qwen/Qwen3-32B",
    "devstral-24b": "mistralai/Devstral-Small-2-24B-Instruct-2512",
    "deepseek-r1-32b": "deepseek-ai/DeepSeek-R1-Distill-Qwen-32B",
}

for name, repo_id in MODELS.items():
    print(f"Downloading {repo_id} → LLM/models/{name}/")
    snapshot_download(repo_id=repo_id, local_dir=f"LLM/models/{name}")
    print(f"Done: {name}")

print("All models downloaded.")
