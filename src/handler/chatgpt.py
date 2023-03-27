from src.function.openai import generate_response, append_mode

# Define a function to handle a slash command interaction
async def chatgpt_process(interaction, message):
    await interaction.response.defer()
    user = str(interaction.user.id)
    # Generate a response using ChatGPT
    response = generate_response(user, message)
    # Send the response back to Discord

    await interaction.followup.send(f"*{message}*\n\n{response}")

#Handles mode change for ChatGPT
async def chatgpt_mode(interaction, mode):
    await interaction.response.defer()
    user = str(interaction.user.id)
    append_mode(user, mode)
    await interaction.followup.send(f"ChatGPT {mode} activated")