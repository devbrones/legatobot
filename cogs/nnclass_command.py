import discord
from discord import client
from discord.embeds import Embed
from discord.ext import commands
import readschedule
from readschedule import nextup, nnextup
from formating import *

class Commands(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command(aliases=['nnext', 'nn', 'nnclass', 'nnc'])
    async def nnextclass(self, ctx, arg=None):
        rh = discord.utils.find(lambda r: r.name == 'Mentor: Hanna', ctx.message.guild.roles)
        rd = discord.utils.find(lambda r: r.name == 'Mentor: Don', ctx.message.guild.roles)

        a_ = csvFormater()

        if not arg:

            #next class (has role Mentor: Hanna)
            if rh in ctx.author.roles:
                a_.csvConvert(nnextup('hanna'))
                #print("2021-08-18 10:15:00+00:00,2021-08-18 11:30:00+00:00,Uppstartsdag 1, Don Magnusson Hanna Åberg - Agenda not available,311")
                print(a_.start, a_.classroom, a_.teachers, a_.agenda)
                embedVar = discord.Embed(title=a_.subject, color=0x0e41b5)
                embedVar.add_field(name="Tid", value=a_.start, inline=False)  
                embedVar.add_field(name="Klassrum", value=a_.classroom, inline=False)  
                embedVar.add_field(name="Lärare", value=a_.teachers, inline=False)  
                embedVar.add_field(name="Agenda", value=a_.agenda, inline=False)  
                embedVar.add_field(name="Uppgift", value=a_.assignment, inline=False)   
                await ctx.send(embed=embedVar)

            #next class (has role Mentor: Don)
            elif rd in ctx.author.roles:
                a_.csvConvert(nnextup('don'))
                print(a_.start, a_.classroom, a_.teachers, a_.agenda)
                embedVar = discord.Embed(title=a_.subject, color=0x0e41b5)
                embedVar.add_field(name="Tid", value=a_.start, inline=False)
                embedVar.add_field(name="Klassrum", value=a_.classroom, inline=False)
                embedVar.add_field(name="Lärare", value=a_.teachers, inline=False)
                embedVar.add_field(name="Agenda", value=a_.agenda, inline=False)
                embedVar.add_field(name="Uppgift", value=a_.assignment, inline=False)
                await ctx.send(embed=embedVar)
                print(a_.start, a_.classroom, a_.teachers, a_.agenda)
        else:

            #.nextclass hanna
            if arg.lower() == 'hanna':
                a_.csvConvert(nnextup('hanna'))
                print(a_.start, a_.classroom, a_.teachers, a_.agenda)
                embedVar = discord.Embed(title=a_.subject, color=0x0e41b5)
                embedVar.add_field(name="Tid", value=a_.start, inline=False)  
                embedVar.add_field(name="Klassrum", value=a_.classroom, inline=False)  
                embedVar.add_field(name="Lärare", value=a_.teachers, inline=False)  
                embedVar.add_field(name="Agenda", value=a_.agenda, inline=False)  
                embedVar.add_field(name="Uppgift", value=a_.assignment, inline=False)  
                await ctx.send(embed=embedVar)
            
            #.nextclass don

            if arg.lower() == 'don':
                a_.csvConvert(nnextup('don'))
                print(a_.start, a_.classroom, a_.teachers, a_.agenda)
                embedVar = discord.Embed(title=a_.subject, color=0x0e41b5)
                embedVar.add_field(name="Tid", value=a_.start, inline=False)  
                embedVar.add_field(name="Klassrum", value=a_.classroom, inline=False)  
                embedVar.add_field(name="Lärare", value=a_.teachers, inline=False)  
                embedVar.add_field(name="Agenda", value=a_.agenda, inline=False)  
                embedVar.add_field(name="Uppgift", value=a_.assignment, inline=False)  
                await ctx.send(embed=embedVar)
            

def setup(client):
    client.add_cog(Commands(client))
