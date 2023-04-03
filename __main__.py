import discord
import json

from discord import app_commands
from src.globals.enums import Moods

from src.handler.chatgpt import chatgpt_process, chatgpt_mood

# Read the JSON file
with open('config/config.json', 'r') as f:
    config = json.load(f)

# Read the commands JSON file
with open('src/globals/commands.json', 'r') as f:
    commands = json.load(f)

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@tree.command(name="chatgpt", description="Talk to ChatGPT", guild=None)
@app_commands.describe(message="message to ChatGPT")
async def chatgpt(interaction, message: str):
    await chatgpt_process(interaction, message)

@tree.command(name="mood", description="ChatGPT mood for you", guild=None)
@app_commands.describe(mood='Select a chat mood')
async def chatgpt(interaction, mood: Moods):
    await chatgpt_mood(interaction, mood.value)

@client.event
async def on_ready():
    await tree.sync(guild=None)
    print("Ready!")

# Run the client
client.run(config["discord"]["TOKEN"])
