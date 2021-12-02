import discord
import readschedule
from readschedule import nextup, nnextup
from formating import *
from discord import client
from discord.ext import commands
from createevent import createEvent, vartoarray


class Commands(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command(aliases=['add'])
    async def cce(self, ctx):
        a_ = csvFormater()
        a_.csvConvert(nextup('hanna'))
        print(a_.start)
        ar = vartoarray(a_.subject,a_.start,a_.finish,a_.classroom,a_.teachers,a_.agenda)
        createEvent(ctx.message.guild.id, ar)
        print(ar)

        await ctx.send("Added a **server event** for class")

def setup(client):
    client.add_cog(Commands(client))
