import os
from espn_api.basketball import League
from dotenv import load_dotenv

config = load_dotenv()

year = 2023
league_id = os.getenv('LEAGUE_ID')
espn_s2 = os.getenv('ESPN_S2')
swid = os.getenv('SWID')

league = League(league_id, year, espn_s2, swid)
top_free_agents = league.free_agents()

def get_help_menu():
    help_menu = '''
INFO: Options and description:
$fa-status     - Top 50 Free Agents and their current health
$injury-report - All players that are currently out 
'''
    return help_menu

def get_free_agents():
    top_free_agents_and_health = []
    for player in top_free_agents:
        x = ('{} - {}'.format(player.name, player.injuryStatus))
        top_free_agents_and_health.append(x)

    formatted_fa = "\n".join(top_free_agents_and_health)
    return formatted_fa

def get_injured_players():
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
    return formatted_injured_players

def get_win_loss():
    all_teams_stats = []
    for team in league.teams:
        current_record = '{} - Win: {} Loss: {}'.format(team.team_name, team.wins, team.losses)
        all_teams_stats.append(current_record)

    formatted_all_team_stats = '\n'.join(all_teams_stats)
    return formatted_all_team_stats
