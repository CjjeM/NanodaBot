from keep_alive import keep_alive
from discord.ext import commands
import discord
import os

intents = discord.Intents.default()
intents.members = True
intents.reactions = True
client = commands.Bot(command_prefix="~shion ", intents=intents)
client.remove_command("help")


def bot_devID(ctx):
    return ctx.message.author.id == int(os.getenv('DEVID'))


@client.command()
@commands.check(bot_devID)
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")


@client.command()
@commands.check(bot_devID)
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")


@client.command()
@commands.check(bot_devID)
async def reload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    client.load_extension(f"cogs.{extension}")


@client.command()
@commands.check(bot_devID)
async def check_cogs(ctx, cog_name):
    try:
        client.load_extension(f"cogs.{cog_name}")
    except commands.ExtensionAlreadyLoaded:
        await ctx.send("Cog is loaded")
    except commands.ExtensionNotFound:
        await ctx.send("Cog not found")
    else:
        await ctx.send("Cog is unloaded")
        client.unload_extension(f"cogs.{cog_name}")


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

keep_alive()
client.run(os.getenv('TOKEN'))
