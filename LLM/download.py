from dotenv import load_dotenv
from huggingface_hub import snapshot_download
load_dotenv()
snapshot_download(repo_id="meta-llama/Llama-3.2-3B-Instruct", local_dir="LLM/model")
