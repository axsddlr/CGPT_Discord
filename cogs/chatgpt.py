import json

import discord
from discord import app_commands
from discord.ext import commands
from revChatGPT.Official import AsyncChatbot

# Opening the config.json file and loading it into the config variable.
with open('config.json', 'r') as f:
    config = json.load(f)

TOKEN = config["DISCORD_TOKEN"]
discord_id = config["discord_id"]
openai_api_key = config['api_key']
chatbot = AsyncChatbot(api_key=openai_api_key)


async def handle_response(message) -> str:
    response = await chatbot.ask(message)
    responseMessage = response["choices"][0]["text"]

    return responseMessage


async def send_message(message, user_message):
    """
    It takes a message and a user message, and sends the response to the message

    :param message: The message object that was sent to the bot
    :param user_message: The message that the user sent
    """
    # Sending the response to the user.
    try:
        # Creating a string that contains the user's message, the user's id, and the response from the chatbot.
        response = '> **' + user_message + '** - <@' + \
                   str(message.user.id) + '> \n\n'
        response = f"{response}{await handle_response(user_message)}"
        # Checking if the response is greater than 1900 characters.
        if len(response) > 1900:
            if "```" in response:
                # It splits the response into parts, and stores it in the parts variable.
                parts = response.split("```")
                # Sending the first part of the response to the user.
                await message.followup.send(parts[0], ephemeral=True)
                # It splits the code block into lines and stores it in the code_block variable.
                code_block = parts[1].split("\n")
                # Initializing the variable formatted_code_block to an empty string.
                formatted_code_block = ""
                # Splitting the code block into lines and storing it in the code_block variable.
                for line in code_block:
                    while len(line) > 1900:
                        # Split the line at the 50th character
                        formatted_code_block += line[:1900] + "\n"
                        line = line[1900:]
                    # Adding the line to the formatted_code_block variable.
                    formatted_code_block += line + "\n"

                # Splitting the code block into chunks of 1900 characters and sending it to the user.
                if len(formatted_code_block) > 2000:
                    code_block_chunks = [formatted_code_block[i:i + 1900]
                                         for i in range(0, len(formatted_code_block), 1900)]
                    for chunk in code_block_chunks:
                        await message.followup.send("```" + chunk + "```", ephemeral=True)
                else:
                    await message.followup.send("```" + formatted_code_block + "```", ephemeral=True)

                # Checking if the response is greater than 1900 characters, and if it is, it splits it into chunks of
                # 1900 characters and sends it to the user.
                if len(parts) >= 3:
                    await message.followup.send(parts[2])
            else:
                response_chunks = [response[i:i + 1900]
                                   for i in range(0, len(response), 1900)]
                for chunk in response_chunks:
                    await message.followup.send(chunk)
        else:
            await message.followup.send(response)
    except Exception as e:
        await message.followup.send("> **Error: Something went wrong, please try again later!**")


class ChatGPT(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="rollback", description='rolls back the chatbot by a specified amount of messages')
    @app_commands.guilds(discord.Object(id=discord_id))
    async def rollback_command(self, ctx):
        """
        It rolls back the chatbot by 1.
        """
        await ctx.response.defer()
        chatbot.rollback(1)
        await ctx.followup.send("Chatbot rolled back by 1 message")

    @app_commands.command(name="reset", description='Chat with the ChatGPT bot')
    @app_commands.guilds(discord.Object(id=discord_id))
    async def reset_command(self, ctx):
        """
        It resets the chatbot.
        """
        await ctx.response.defer()
        chatbot.reset()
        await ctx.followup.send("Chatbot has been reset")

    @app_commands.command(name="chatgpt", description='Chat with the ChatGPT bot')
    @app_commands.describe(message="insert word or phrase that response will be based on")
    @app_commands.guilds(discord.Object(id=discord_id))
    async def cgpt(self, ctx: discord.Interaction, *, message: str):
        """
        `async def cgpt(self, ctx: discord.Interaction, *, message: str):`

        The `async` keyword is used to define an asynchronous function

        :param ctx: The context of the message
        :type ctx: discord.Interaction
        :param message: str - The message to send to the chatbot
        :type message: str
        """
        await ctx.response.defer()
        await send_message(ctx, message)


async def setup(bot):  # set async function
    await bot.add_cog(ChatGPT(bot))
