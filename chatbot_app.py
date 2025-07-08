from openai import OpenAI
from dotenv import load_dotenv
import os



#load_dotenv()   # load .env file


client = OpenAI()

# response = client.responses.create(
#     model="gpt-4.1-nano"
# )
# completion = client.chat.completions.create(
#   model="gpt-4.1-nano",
#   store=True,
#   messages=[
#     {"role": "user", "content": "write a haiku about ai"}
#   ]
# )

# print(completion.choices[0].message);

response = client.responses.create(
    model="gpt-4.1-nano",
    input="what is your name?"
)

print(response.output_text)