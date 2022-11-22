import click
import espn_responses
import discord_bot

@click.command()
def discord():
    discord_bot.run()

@click.command()
def fa():
    print(espn_responses.get_free_agents())

@click.command()
def injuries():
    print(espn_responses.get_injured_players())

@click.command()
def teamstats():
    print(espn_responses.get_win_loss())
    
@click.command()
def scoreboard():
    print(espn_responses.get_score_board())

@click.group
def commands():
    pass

commands.add_command(discord)
commands.add_command(fa)
commands.add_command(injuries)
commands.add_command(teamstats)
commands.add_command(scoreboard)


