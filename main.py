import argparse
import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

# Loads API Key
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

# Loads API Key into Google GenAI
client = genai.Client(api_key=api_key)

# Allows user input in content generation
parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("prompt", type=str, help="Enter your prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()

messages = [types.Content(role="user", parts=[types.Part(text=args.prompt)])]

# Generates content based on user input
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=messages,
)

# Prints API response and token counts
if response.usage_metadata is None:
    raise RuntimeError("API request failed - check your token count")
if args.verbose:
    print(f"User prompt: {args.prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
print(f"Response: {response.text}")


def main():
    print("Hello from AIAgent!")


if __name__ == "__main__":
    main()
