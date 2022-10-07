import os
from espn_api.basketball import League

league_id = 2029761943
year = 2023
espn_s2 = os.environ["ESPN_S2"] 
swid = os.environ["SWID"]
discord_secret = os.environ["DISCORD_SECRET"]

league = League(league_id, year, espn_s2, swid)

print('INFO: TEAMS')
print(league.teams)
print('INFO: FREE AGENTS')

pro_players_data = league.free_agents()
all_players = []
injured_players = []
free_agency_status = []

for player in pro_players_data:
    x = ('{} - {}'.format(player.name, player.injuryStatus))
    free_agency_status.append(x)

formatted_fa = "\n".join(free_agency_status)

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