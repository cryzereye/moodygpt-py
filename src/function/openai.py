import openai
import json

with open('src/globals/constants.json', 'r') as f:
    constants = json.load(f)

with open('config/config.json', 'r') as f:
    config = json.load(f)

with open('config/userdata.json', 'r') as f:
    userdata = json.load(f)

# Set up OpenAI API credentials
openai.api_key = config["openai"]["SECRET_KEY"]

# Define a function to send a message to ChatGPT and return the response
def generate_response(user, prompt):

    new_msg = {"role": "user", "content": prompt}
    history = fetch_data(user)
    print("\n\n")
    print(history)
    history.append(new_msg)
    print("\n\n")
    print(history)
    
    response = openai.ChatCompletion.create(
        model=constants["openai"]["model"],
        messages=history,
        max_tokens=1024,
        n=2,
        stop=None,
        temperature=0.3,
        user=user
    )

    if(response):
        save_message(user, new_msg)
        save_message(user, {"role" : "assistant", "content" : response.choices[0].message.content})
        return response.choices[0].message.content
    return "Was not able to communicate with ChatGPT"

def fetch_data(user):
    messages = []
    if(user in userdata):
        messages = userdata[user]
    return messages

def save_message(user, message):
    if(not(user in userdata)):
        userdata[user] = []
    userdata[user].append(message)

    with open('config/userdata.json', 'w') as f:
        json.dump(userdata, f)