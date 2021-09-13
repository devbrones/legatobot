import discord
from discord import client
from discord.ext import commands

class Commands(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if after.channel is not None:
            if after.channel.name == "Skapa VC":
                await after.channel.category.create_voice_channel("VC")
                vc = after.channel.category.voice_channels[len(after.channel.category.voice_channels) - 1]

                await member.move_to(vc)

        if before.channel is not None:
            if before.channel.name != "Skapa VC" and self.client.get_channel(before.channel.id).members == [] and before.channel.name == "VC":
                await before.channel.delete()

def setup(client):
    client.add_cog(Commands(client))