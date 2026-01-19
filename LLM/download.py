from dotenv import load_dotenv
from huggingface_hub import snapshot_download
load_dotenv()
snapshot_download(repo_id="mistralai/Devstral-Small-2-24B-Instruct-2512", local_dir="LLM/model")
