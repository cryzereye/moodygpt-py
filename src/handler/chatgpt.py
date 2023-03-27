from src.function.openai import generate_response

# Define a function to handle a slash command interaction
async def chatgpt_process(interaction, message):
    await interaction.response.defer()
    user = str(interaction.user.id)
    # Get the argument value from the interaction
    argument = 'start your answer with "Actually,".' + message
    # Generate a response using ChatGPT
    response = generate_response(user, argument)
    # Send the response back to Discord

    await interaction.followup.send(f"*{message}*\n\n{response}")