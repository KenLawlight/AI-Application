from openai import OpenAI
client = OpenAI()

prompt = """Replace car with plane and adjust phrase:
A car is a vehicle that is typically powered by an internal combustion engine or an electric motor. It has four wheels, and is designed to carry passengers and/or cargo on roads or highways. Cars have become a ubiquitous part of modern society, and are used for a wide variety of purposes, such as commuting, travel, and transportation of goods. Cars are often associated with freedom, independence, and mobility."""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    max_completion_tokens=100
)

print("=== FIND & REPLACE RESULT ===")
print(response.choices[0].message.content)


finance_text = """
The company reported a significant increase in quarterly revenue due 
to strong sales in its technology division. Operating costs rose slightly 
because of increased investment in research and development. Despite these 
expenses, net profit margins improved and analysts expect continued growth 
throughout the year.
"""

prompt = f"""Summarize the following text into two concise bullet points:
{finance_text}"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    max_completion_tokens=400
)

print("\n=== SUMMARY RESULT ===")
print(response.choices[0].message.content)


max_completion_tokens = 500

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Cost calculation example"}],
    max_completion_tokens=max_completion_tokens
)

input_token_price = 0.15 / 1_000_000
output_token_price = 0.6 / 1_000_000

input_tokens = response.usage.prompt_tokens
output_tokens = max_completion_tokens

cost = (input_tokens * input_token_price) + (output_tokens * output_token_price)

print("\n=== COST ESTIMATION ===")
print(f"Input tokens: {input_tokens}")
print(f"Output tokens (max): {output_tokens}")
print(f"Estimated cost: ${cost}")