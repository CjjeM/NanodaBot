from discord.ext import commands
import discord

@commands.command(aliases=["hug"])
async def HugTimeFunTime(self, ctx):
    await ctx.send(file=discord.File('./sources/hug.png'))