import openai
import json

with open('src/globals/constants.json', 'r') as f:
    constants = json.load(f)

with open('config/config.json', 'r') as f:
    config = json.load(f)

# Set up OpenAI API credentials
openai.api_key = config["openai"]["SECRET_KEY"]

# Define a function to send a message to ChatGPT and return the response
def generate_response(user, prompt):
    response = openai.ChatCompletion.create(
        model=constants["openai"]["model"],
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1024,
        n=2,
        stop=None,
        temperature=0.3,
        user=user
    )
    return response.choices[0].message.content