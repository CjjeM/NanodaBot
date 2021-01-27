from discord.ext import commands
import discord
from random import choice

emojis = ['fist', 'raised_hand', 'v']

class Game(commands.Cog):
  def __init__(self, client):
    self.client = client
  
  def check_win_condition(self, emoji):
    shion_choices = ['R', 'P', 'S']
    emoji_parser = {'✊': 'R', '✋': 'P', '✌': 'S'}
    win_conditions = [['P', 'R'], ['R', 'S'], ['S', 'P']]
    user = emoji_parser[str(emoji)]
    shion = choice(shion_choices)

    game_condition = [user, shion]
    
    for condition in win_conditions:
      if game_condition == condition:
        return True
      elif game_condition == list(reversed(condition)):
        return False
    
    else:
      return "Tie"
  
  @commands.command(aliases=["rps", "jkp"])
  async def rpsGame(self, ctx):
    # Initialization of RPS game
    game = discord.Embed(title="Jankenpon with Shion!", description="Please choose from the three emojis within 10 secs")

    emojis = ['\u270A', '\u270B', '\u270C']
    game = await ctx.send(embed=game)
    for emoji in emojis:
      await game.add_reaction(emoji)
    
    #Getting user reactions
    def user_choice(reaction, user):
      return user == ctx.message.author and str(reaction.emoji) in emojis

    try:
      reaction, user = await self.client.wait_for('reaction_add', timeout=10, check=user_choice)
    except:
      await ctx.send("10 secs has passed. Shion wins. ez")
    else:
      condition = self.check_win_condition(reaction.emoji)

      if condition:
        await ctx.send("You win!")
      elif condition == "Tie":
        await ctx.send("It's a Tie!")
      else:
        await ctx.send("Shion wins!")
    
  
def setup(client):
  client.add_cog(Game(client))