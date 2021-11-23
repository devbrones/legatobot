import discord
from discord import client
from discord.embeds import Embed
from discord.ext import commands
import readschedule
from readschedule import compTime
from formating import *

async def compclass():
    a_ = csvFormater()
    a_.csvConvert(compTime('don'))
    print(a_.start, a_.classroom, a_.teachers, a_.agenda)
    embedVar = discord.Embed(title=a_.subject, color=0x0e41b5)
    embedVar.add_field(name="Tid", value=a_.start, inline=False)
    embedVar.add_field(name="Klassrum", value=a_.classroom, inline=False)
    embedVar.add_field(name="Lärare", value=a_.teachers, inline=False)
    embedVar.add_field(name="Agenda", value=a_.agenda, inline=False)
    embedVar.add_field(name="Uppgift", value=a_.assignment, inline=False)
    await ctx.send(embed=embedVar)
    print(a_.start, a_.classroom, a_.teachers, a_.agenda)
