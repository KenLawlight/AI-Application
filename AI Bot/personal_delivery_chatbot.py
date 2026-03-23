import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OpenAI API key not found in .env file")

def get_response(system_prompt, user_prompt):
    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        max_tokens=400
    )
    return response.choices[0].message.content

service_description = """MyPersonalDelivery is a fast and reliable delivery service that helps customers
send and receive everyday items with ease. The service delivers groceries,
medicines, electronics, clothing, documents, and small household items.

MyPersonalDelivery offers same-day delivery for groceries and medicines in most
cities, affordable pricing, real-time order tracking, and friendly customer
support. The goal of the service is to make daily deliveries simple, safe, and
stress-free for customers."""

system_prompt = f"""You are a customer service chatbot for MyPersonalDelivery whose service description is delimited by triple backticks.
You should respond to user queries in a gentle and helpful way.
```{service_description}```"""

user_prompt = "What benefits does MyPersonalDelivery offer?"

response = get_response(system_prompt, user_prompt)

print(response)