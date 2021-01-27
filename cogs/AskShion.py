from discord.ext import commands
import discord
from random import choice
import re


class AskShion(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["ask"], pass_context=True)
    async def askShion(self, ctx, *, message: str):
        choices = re.split(r"\bor\b", message)
        await ctx.send(f"Shion says, {choice(choices).strip()}")

    @askShion.error
    async def askShion_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            if error.param.name == 'message':
                await ctx.send("Please fill in the choices to choose from")


def setup(client):
    client.add_cog(AskShion(client))
