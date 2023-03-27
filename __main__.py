import discord
import openai
import json

from discord import app_commands

# Read the JSON file
with open('config/config.json', 'r') as f:
    config = json.load(f)

# Read the commands JSON file
with open('src/globals/commands.json', 'r') as f:
    commands = json.load(f)

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

# Set up OpenAI API credentials
openai.api_key = config["openai"]["SECRET_KEY"]
model_engine = 'gpt-3.5-turbo'

# Define a function to send a message to ChatGPT and return the response
def generate_response(prompt):

    response = openai.ChatCompletion.create(
        model=model_engine,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1024,
        n=2,
        stop=None,
        temperature=0.3
    )
    return response.choices[0].message.content

@tree.command(name="chatgpt", description="Talk to ChatGPT", guild=discord.Object(config["server"]["ID"]))
@app_commands.describe(message="message to ChatGPT")
async def chatgpt(interaction, message: str):
    await ai(interaction, message)

# Define a function to handle a slash command interaction
async def ai(interaction, message):
    await interaction.response.defer()

    # Get the argument value from the interaction
    argument = 'start your answer with "Actually,".' + message
    # Generate a response using ChatGPT
    response = generate_response(argument)
    # Send the response back to Discord

    await interaction.followup.send(f"*{message}*\n\n{response}")


@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=config["server"]["ID"]))
    print("Ready!")

# Run the client
client.run(config["discord"]["TOKEN"])
