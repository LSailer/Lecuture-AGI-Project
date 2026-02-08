import os
import asyncio
from dotenv import load_dotenv
from google import genai

# Load env variables (api keys)
load_dotenv()


async def test_gemini():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY not found in .env")
        return

    print(f"Testing Gemini API with key ending in ...{api_key[-4:]}")

    try:
        client = genai.Client(api_key=api_key)
        model_id = "gemini-2.5-flash"

        print(f"Sending request to {model_id}...")
        response = await client.aio.models.generate_content(
            model=model_id,
            contents="Hello, are you working?",
        )
        print("\nResponse Received:")
        print(response.text)
        print("\nAPI Connection Successful!")

    except Exception as e:
        print(f"\nAPI Connection Failed: {e}")


if __name__ == "__main__":
    asyncio.run(test_gemini())
