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
        max_tokens=300
    )
    return response.choices[0].message.content

prompt = """
I need to plan for my 2 week beach vacation.
step 1: Four potential locations.
step 2: Each location must have accommodation options, some activities.
step 3: Evaluate pros and cons for each location.
"""

response = get_response(prompt)
print(response)