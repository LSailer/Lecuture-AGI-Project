from dotenv import load_dotenv
from huggingface_hub import snapshot_download
load_dotenv()
snapshot_download(repo_id="Qwen/Qwen3-30B-A3B-Instruct-2507", local_dir="LLM/model")
