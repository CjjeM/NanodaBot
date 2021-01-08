
import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix = "~shion ")

@client.event
async def on_ready():
  print("aight bot login lezgo, backendwkwkwkwk")

@client.command(aliases=["greet"])
async def gudShionMessage(ctx):
  await ctx.send(f"love yaaa!")

@client.command(aliases=['pat'])
async def hedpatPowerSupreme(ctx):
  await ctx.send(file=discord.File('pat.png'))

client.run(os.getenv('TOKEN'))
