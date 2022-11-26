import click
import espn_responses
import discord_bot

@click.command()
def discord():
    """Run discord bot"""
    discord_bot.run()

@click.command()
def fa():
    """Get top 50 free agents"""
    print(espn_responses.get_free_agents())

@click.command()
def injuries():
    """Get top 50 injured playeres"""
    print(espn_responses.get_injured_players())

@click.command()
def teamstats():
    """Get record for all fantasy league teams"""
    print(espn_responses.get_win_loss())
    
@click.command()
def scoreboard():
    """Get score for this week's fantasy league matchups"""
    print(espn_responses.get_score_board())

@click.group
def commands():
    """CLI for interfacing with an ESPN NBA fantasy league"""
    pass

commands.add_command(discord)
commands.add_command(fa)
commands.add_command(injuries)
commands.add_command(teamstats)
commands.add_command(scoreboard)


