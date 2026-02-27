import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("Open api key not found from env files")

def get_response(promt):
    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        max_completion_tokens=100,
        messages=[{"role":"user", "content" : promt}]

    )
    return response.choices[0].message.content

response = get_response("EXplain about different role, user, system and, use bullet points for your response ")

print(response)
