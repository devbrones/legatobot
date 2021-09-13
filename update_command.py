import discord
from discord import client
from discord.ext import commands
from readschedule import cleanCSV

class Commands(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['u', 'update'])
    async def clean(self, ctx):
        cleanCSV("hanna")
        cleanCSV("don")
        await ctx.send("Cleansed the CSV <3")

def setup(client):
    client.add_cog(Commands(client))
