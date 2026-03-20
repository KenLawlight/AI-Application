import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OpenAI API key not found in .env file")

# A get_response() that accepts system + user prompts
def get_response(system_prompt, user_prompt):
    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        max_tokens=300
    )
    return response.choices[0].message.content


# -------- ROLE-PLAYING PROMPT EXERCISE --------

system_prompt = (
    "You are a knowledgeable and supportive learning advisor. "
    "Your role is to interpret user queries by understanding their background, "
    "experience level, and learning goals. Based on this information, "
    "recommend appropriate textbooks, including both beginner-level and advanced materials. "
    "Provide recommendations that match their skill level and learning objectives."
)

user_prompt = (
    "Hello there! I'm a beginner with a marketing background, and I'm really "
    "interested in learning about Python, data analytics, and machine learning. "
    "Can you recommend some books?"
)

response = get_response(system_prompt, user_prompt)
print(response)