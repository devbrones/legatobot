import discord
from discord import client
from discord.ext import commands

class Commands(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command(aliases=['sus'])
    async def susy(self, ctx):
        with open('sus.gif', 'rb') as f:
            picture = discord.File(f)
            await ctx.send(file=picture)
            await ctx.send("我一连几个小时都带着微笑吮吸他的鸡巴\n盯着他的胡说八道，而我今晚抑制住我的精液\n当他问我什么姿势时，我说“Doggystyle”\n（当他们问我什么姿势时，我说“Doggystyle”）")

def setup(client):
    client.add_cog(Commands(client))
