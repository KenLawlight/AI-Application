import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OpenAI API key not found in .env file")

client = OpenAI()

messages = [
    {
        "role": "system",
        "content": "You are a helpful math tutor that speaks concisely."
    }
]

user_msgs = [
    "Explain what pi is.",
    "Why is pi important in mathematics?",
    "Summarize the explanation in one sentence."
]

for msg in user_msgs:

    user_dict = {
        "role": "user",
        "content": msg
    }

    messages.append(user_dict)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        max_completion_tokens=100
    )

    assistant_dict = {
        "role": "assistant",
        "content": response.choices[0].message.content
    }

    messages.append(assistant_dict)

    print("User:", msg)
    print("Assistant:", assistant_dict["content"])
    print()

print(messages)