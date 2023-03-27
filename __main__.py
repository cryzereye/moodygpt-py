import discord
import json

from discord import app_commands
from src.globals.enums import Modes

from src.handler.chatgpt import chatgpt_process, chatgpt_mode

# Read the JSON file
with open('config/config.json', 'r') as f:
    config = json.load(f)

# Read the commands JSON file
with open('src/globals/commands.json', 'r') as f:
    commands = json.load(f)

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@tree.command(name="chatgpt", description="Talk to ChatGPT", guild=discord.Object(config["server"]["ID"]))
@app_commands.describe(message="message to ChatGPT")
async def chatgpt(interaction, message: str):
    await chatgpt_process(interaction, message)

@tree.command(name="chatgpt_mode", description="Talk to ChatGPT", guild=discord.Object(config["server"]["ID"]))
@app_commands.describe(mode='Enter a chat mode')
async def chatgpt(interaction, mode: Modes):
    await chatgpt_mode(interaction, mode.value)

@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=config["server"]["ID"]))
    print("Ready!")

# Run the client
client.run(config["discord"]["TOKEN"])
