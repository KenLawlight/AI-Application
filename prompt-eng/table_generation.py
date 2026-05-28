import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def get_response(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content


prompt1 = (
    "Generate a table containing 10 must-read science fiction books for a sci-fi lover. "
    "The table must have columns: Title, Author, Year."
)

response1 = get_response(prompt1)
print(response1)


text2 = """
Artificial Intelligence is transforming the way people work and communicate. 
From healthcare to education, AI-powered tools are helping solve complex problems 
faster and more efficiently. Many companies are now investing heavily in AI research 
to build smarter applications for the future.
"""

instructions2 = (
    "Determine the language of the following text and generate a suitable title for it. "
    "The text will be provided inside triple backticks."
)

output_format2 = (
    "Text:\n"
    "Language:\n"
    "Title:"
)

prompt2 = f"""
{instructions2}

Output format:
{output_format2}

Text:
```{text2}```
"""

response2 = get_response(prompt2)
print(response2)


text3 = """
Machine learning is changing industries worldwide. It enables systems to learn from data 
and improve over time. This shift is dramatically increasing efficiency in many sectors.
"""

instructions3 = (
    "Determine the language of the given text and count the number of sentences. "
    "If the text has more than one sentence, generate a suitable title. "
    "If it has only one sentence, write 'N/A' for the title. "
    "Text will be inside triple backticks."
)

output_format3 = (
    "Text:\n"
    "Language:\n"
    "Number of sentences:\n"
    "Title:"
)

prompt3 = instructions3 + "\n" + output_format3 + f"\n```{text3}```"

response3 = get_response(prompt3)
print(response3)