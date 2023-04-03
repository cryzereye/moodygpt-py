from src.function.openai import generate_response

# Define a function to handle a slash command interaction
async def chatgpt_process(interaction, message):
    await interaction.response.defer()
    user = str(interaction.user.id)
    # Generate a response using ChatGPT
    response = generate_response(user, message)
    # Send the response back to Discord

    await interaction.followup.send(f"*{message}*\n\n{response}")

#Handles mood change for ChatGPT
async def chatgpt_mood(interaction, mood):
    await interaction.response.defer()
    user = str(interaction.user.id)
    await interaction.followup.send(f"ChatGPT {mood} activated for <@{user}>")