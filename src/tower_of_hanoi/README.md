# Lecture-AGI-Project

This project implements a Tower of Hanoi solver using an LLM-based agent with decomposition strategies.

## Prerequisites

- **Python**: >= 3.13
- **Hugging Face Account**: You need a valid token to download models (e.g., Llama 3.2).

## Installation

1.  **Install Dependencies**:
    This project uses `uv` for dependency management.

    ```bash
    uv sync
    ```

    _Alternatively, using pip:_

    ```bash
    pip install -e .
    pip install python-dotenv huggingface_hub
    ```

## Configuration

1.  Create a `.env` file in the root directory.
2.  Add your Hugging Face token to `.env`:

    ```env
    HF_TOKEN=hf_...
    ```

    > **Note**: Ensure you have access to the model defined in `LLM/download.py` (default: `meta-llama/Llama-3.2-3B-Instruct`) on Hugging Face. You may need to accept the license agreement on the model card page.

## Usage

### 1. Download the LLM

First, download the model weights to the local directory.

```bash
python LLM/download.py
```

This will download the model to `LLM/model`.

### 2. Run the Simulation

Run the main script from the root directory:

```bash
python tower_of_hanoi/main.py
```

This will:

- Initialize the Tower of Hanoi environment.
- Start the LLM-based agent.
- Log progress and save action distribution plots to the `output/` folder.
