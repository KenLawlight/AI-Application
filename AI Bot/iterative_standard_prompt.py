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
        max_tokens=400
    )
    return response.choices[0].message.content

prompt = """
Create a table with three columns: Model Name, Release Year, Owning Company.
List the top ten pre-trained language models.
The output must be formatted as a clean text table.
"""

response = get_response(prompt)
print(response)