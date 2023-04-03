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
    mood = get_mood_data(get_user_mood(user))
    fullMsg = mood.append(new_msg)

    response = openai.ChatCompletion.create(
        model=constants["openai"]["model"],
        messages=fullMsg,
        max_tokens=4096,
        n=2,
        stop=None,
        temperature=0.3,
        user=user
    )

    if(response):
        return response.choices[0].message.content
    return "Was not able to communicate with ChatGPT"

def save_mood(user, mood):
    if(not(user in userdata)):
        userdata[user] = {}
    userdata[user]["mood"] = mood

    with open('config/userdata.json', 'w') as f:
        json.dump(userdata, f)


# Mood handling
def get_mood_data(mood):
    if(mood in constants["openai"]["moods"]):
        return constants["openai"]["moods"][mood]
    else: []

def get_user_mood(user):
    if(not(user in userdata)):
        save_mood(user, "reset")
    return userdata[user]["mood"]