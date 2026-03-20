
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

product_description = "A compact smart home security camera with night vision, motion detection, and mobile app integration for real-time alerts."

prompt = f"""
Expand the following product description into a single, comprehensive paragraph.
The paragraph must clearly explain the product’s unique features, its benefits to the user,
and the potential applications in real-world scenarios.

Product Description:
{product_description}
"""

response = get_response(prompt)
print(response)