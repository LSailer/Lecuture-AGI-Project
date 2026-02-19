from dotenv import load_dotenv
from huggingface_hub import snapshot_download
load_dotenv()
snapshot_download(repo_id="Qwen/Qwen3-14B", local_dir="LLM/model")
