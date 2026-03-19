import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
 
if not api_key:
    raise ValueError("Open api key not found frin env file")

def get_response(prompt):
    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    return response.choices[0].message.content

prompt = """
Q: Extract the odd numbers from {1, 3, 7, 12, 19}. A: Odd numbers = {1, 3, 7, 19}
Q: Extract the odd numbers from {3, 5, 11, 12, 16}. A:
"""

response = get_response(prompt)
print(response)