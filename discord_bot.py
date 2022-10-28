import os
import discord
import espn_responses
from dotenv import load_dotenv

config = load_dotenv()

def run():
    discord_secret = os.getenv('DISCORD_SECRET')
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'We have logged in as {client.user}')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message.content.startswith('$help') or message.content.startswith('$h'):
            await message.channel.send('```\n{}\n```'.format(espn_responses.get_help_menu()))

        if message.content.startswith('$fa-status'):
            await message.channel.send('```\n{}\n```'.format(espn_responses.get_free_agents()))
        
        if message.content.startswith('$injury-report'):
            await message.channel.send('```\n{}\n```'.format(espn_responses.get_injured_players()))

        if message.content.startswith('$team-stats'):
            await message.channel.send('```\n{}\n```'.format(espn_responses.get_win_loss()))

    client.run(discord_secret)