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
    history = fetch_data(user, new_msg)
    history.append(new_msg)
    
    response = openai.ChatCompletion.create(
        model=constants["openai"]["model"],
        messages=history,
        max_tokens=4096,
        n=2,
        stop=None,
        temperature=0.7,
        user=user
    )

    if(response):
        save_message(user, {"role" : "assistant", "content" : response.choices[0].message.content})
        return response.choices[0].message.content
    return "Was not able to communicate with ChatGPT"

def fetch_data(user, message):
    history = []
    if(user in userdata):
        history = userdata[user]["history"]
    else:
        save_message(user, message)
    return history

def save_message(user, message):
    if(not(user in userdata)):
        userdata[user] = {"mode" : "reset", "history" : []}
    userdata[user]["history"].append(message)

    with open('config/userdata.json', 'w') as f:
        json.dump(userdata, f)


# Mode handling
def get_mode(mode):
    if(mode in constants["openai"]["modes"]):
        return constants["openai"]["modes"][mode]
    else: []

def append_mode(user, mode):
    mode_messages = get_mode(mode)
    for msg in mode_messages:
        save_message(user, msg)