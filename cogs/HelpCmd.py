from discord.ext import commands
import discord


class HelpCmd(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.client.remove_command("help")
    
    @commands.command(aliases=["help"])
    async def helpCommand(self, ctx):
        helpEmbed = discord.Embed(title="Help", description="Here are the commands available:", color=0x702593)
        helpEmbed.add_field(name="Give Shion a Headpat", value="~shion pat", inline=True)
        helpEmbed.add_field(name="Make Shion greet you", value="~shion greet", inline=True)
        helpEmbed.add_field(name="Play Jankenpon with Shion", value="~shion rps or ~shion jkp", inline=False)
        helpEmbed.add_field(name="Launch the Help Menu", value="~shion help", inline=False)

        await ctx.send(embed=helpEmbed)

def setup(client):
    client.add_cog(HelpCmd(client))
