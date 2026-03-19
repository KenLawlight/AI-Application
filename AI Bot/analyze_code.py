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
        max_tokens=200
    )
    return response.choices[0].message.content

code = '''
def calculate_rectangle_area(length, width):
    area = length * width
    return area
'''

prompt = f"""
assess the function provided in the delimited code string.
step 1: check for correct syntax.
step 2: receiving two inputs, 5 and 9.
step 3: returning one output.

{code}
"""

response = get_response(prompt)
print(response)