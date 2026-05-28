from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI()

messages = [
    {"role": "system", "content": "You are a helpful math tutor that speaks concisely."}
]

def ask_model(prompt):
    messages.append({"role": "user", "content": prompt})
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        max_completion_tokens=100
    )
    reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    return reply

user_msgs = [
    "Explain what pi is.",
    "Summarize this in two bullet points."
]

for q in user_msgs:
    print("User:", q)
    print("Assistant:", ask_model(q))
    print()

print(messages)