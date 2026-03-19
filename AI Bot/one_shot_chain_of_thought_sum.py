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

example = """Q: Sum the even numbers in the following set: {9, 10, 13, 4, 2}.
A: Even numbers: (10,4,2). Adding them: 10+4+2=16"""

question = """Q: Sum the even numbers in the following set: {15, 13, 82, 7, 14}.
A: Even numbers:"""

prompt = f"""
{example}

{question}
"""

response = get_response(prompt)
print(response)