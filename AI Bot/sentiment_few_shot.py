import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
 
if not api_key:
    raise ValueError("Open api key not found frin env file")

client = OpenAI(api_key=api_key)
response = client.chat.completions.create(
  model = "gpt-4o-mini",
  messages = [
      {"role": "user", "content": "The product quality exceeded my expectations"},
      {"role": "assistant", "content": "1"},
      {"role": "user", "content": "I had a terrible experience with this product's customer service"},
      {"role": "assistant", "content": "-1"},
      {"role": "user", "content": "The price of the product is really fair given its features"}
  ],
  temperature = 0
)

print(response.choices[0].message.content)