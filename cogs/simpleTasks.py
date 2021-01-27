from discord.ext import commands
import discord


class SimpleTasks(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("aight bot login lezgo, backendwkwkwkwk")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        ment = member.mention
        generalChannel = 789156432767352857
        await self.client.get_channel(generalChannel).send(
            f"Hello! Welcome Nanoda! {ment}",
            file=discord.File('./sources/aa.png'))

    @commands.command(aliases=["greet"])
    async def gudShionMessage(self, ctx):
        await ctx.send(f"love yaaa!")

    @commands.command(aliases=['pat'])
    async def hedpatPowerSupreme(self, ctx):
        await ctx.send(file=discord.File('./sources/pat.png'))


def setup(client):
    client.add_cog(SimpleTasks(client))
