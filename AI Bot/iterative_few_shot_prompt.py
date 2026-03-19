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
        messages=[{"role":"user","content":prompt}],
        max_tokens=300
    )
    return response.choices[0].message.content

prompt = """
Classify the emotion in the text. Use only: happiness, sadness, fear, no explicit emotion.

Examples:
Text: "I got the job today!" -> happiness
Text: "I miss my family so much." -> sadness
Text: "Walking alone at night makes me nervous." -> fear
Text: "Time flies like an arrow." -> no explicit emotion
Text: "They sat and ate their meal" ->
"""

response = get_response(prompt)
print(response)