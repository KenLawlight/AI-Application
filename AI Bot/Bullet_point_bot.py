import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OpenAI API key not found in .env file")

def get_response(prompt):
    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are a code reviewer. Point out mistakes and suggest improvements politely."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

print(get_response("def add(a,b): return a+b"))