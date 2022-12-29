import json
import os

import requests
from discord.ext import commands

with open('config.json', 'r') as f:
    config = json.load(f)

url = f"http://{config['ip']}:{config['port']}/api/ask"
headers = {'Authorization': str(config['api_key'])}


class ChatGPT(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @staticmethod
    def process_message(message):
        # define a default value for the data variable
        data = {'content': message}

        # check if response.json file exists
        if os.path.exists('response.json'):
            # load the response from the file
            with open('response.json', 'r') as f:
                response_data = json.load(f)

            # check if response_id and conversation_id have values in the response
            if response_data.get('response_id') and response_data.get('conversation_id'):
                # update the data dictionary with the response_id and conversation_id values
                data.update({
                    'conversation_id': response_data['conversation_id'],
                    'parent_id': response_data['response_id']
                })

        # send the request with the data dictionary
        response = requests.post(url, headers=headers, json=data)

        # save the response to the response.json file
        with open('response.json', 'w') as f:
            json.dump(response.json(), f)

        # return the content from the response
        # return response.json()['content']

        return response.json().get('content', 'No content available, Try again')

    @commands.command(name='chat', aliases=['chatgpt'], description='Chat with the chatgpt model')
    async def echo(self, ctx, *, message: str):
        response = self.process_message(message)

        # send the response back to the channel
        await ctx.send(response)


async def setup(bot):  # set async function
    await bot.add_cog(ChatGPT(bot))
