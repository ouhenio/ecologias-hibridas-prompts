import openai
import os

from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.environ["OPENAI_API_KEY"]

model = "gpt-3.5-turbo-0613"

messages = [
    {
    "role": "system",
    "content": """
    Your role is to generate a very short visual description of a scene including the concepts mentioned by the user
    """
    },
    {
    "role": "user",
    "content": """
    Democracy, antropocene, gobal warming.
    """
    }
]

result = openai.ChatCompletion.create(
    model=model,
    messages=messages,
    temperature=0.7,
    max_tokens=100,
)

print(result["choices"][0]["message"]["content"])