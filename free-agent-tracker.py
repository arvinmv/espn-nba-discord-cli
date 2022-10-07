import os
from espn_api.basketball import League

league_id = 2029761943
year = 2023
espn_s2 = os.environ["ESPN_S2"] 
swid = os.environ["SWID"]
discord_secret = os.environ["DISCORD_SECRET"]

league = League(league_id, year, espn_s2, swid)

top_free_agents = league.free_agents()
top_free_agents_and_health = []

for player in top_free_agents:
    x = ('{} - {}'.format(player.name, player.injuryStatus))
    top_free_agents_and_health.append(x)

formatted_fa = "\n".join(top_free_agents_and_health)

import discord

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

    if message.content.startswith('$fa-status'):
        await message.channel.send('```\n{}\n```'.format(formatted_fa))

client.run(discord_secret)