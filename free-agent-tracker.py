import os
import json
from espn_api.basketball import League

league_id = 2029761943
year = 2023
espn_s2 = os.environ["ESPN_S2"] 
swid = os.environ["SWID"]
discord_secret = os.environ["DISCORD_SECRET"]

league = League(league_id, year, espn_s2, swid)

help_menu = '''
INFO: Options and description:
$fa-status     - Top 50 Free Agents and their current health
$injury-report - All players that are currently out 
'''

# Free Agents - Status
top_free_agents = league.free_agents()
top_free_agents_and_health = []

for player in top_free_agents:
    x = ('{} - {}'.format(player.name, player.injuryStatus))
    top_free_agents_and_health.append(x)

formatted_fa = "\n".join(top_free_agents_and_health)

# Injured Players
injured_players = []

for team in league.teams:
    for player in team.roster:
        if player.injuryStatus == 'OUT' or player.injuryStatus == 'DAY_TO_DAY':
            x = ('{} - {} - {}'.format(player.name, player.injuryStatus, team))
            injured_players.append(x)

for player in top_free_agents:
    if player.injuryStatus == 'OUT' or player.injuryStatus == 'DAY_TO_DAY':
        x = ('{} - {} - Free Agent'.format(player.name, player.injuryStatus))
        injured_players.append(x)

formatted_injured_players = "\n".join(injured_players)

# Win Loss
all_teams_stats = []
for team in league.teams:
    current_record = '{} - Win: {} Loss: {}'.format(team.team_name, team.wins, team.losses)
    all_teams_stats.append(current_record)

formatted_all_team_stats = '\n'.join(all_teams_stats)


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

    if message.content.startswith('$help') or message.content.startswith('$h'):
        await message.channel.send('```\n{}\n```'.format(help_menu))

    if message.content.startswith('$fa-status'):
        await message.channel.send('```\n{}\n```'.format(formatted_fa))
    
    if message.content.startswith('$injury-report'):
        await message.channel.send('```\n{}\n```'.format(formatted_injured_players))

    if message.content.startswith('$team-stats'):
        await message.channel.send('```\n{}\n```'.format(formatted_all_team_stats))

client.run(discord_secret)