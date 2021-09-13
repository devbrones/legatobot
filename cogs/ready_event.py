import discord
from discord import client
from discord.ext import commands
from main import *

class Events(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        update.start()
        read.start()
        print('Bot online')

def setup(client):
    client.add_cog(Events(client))
