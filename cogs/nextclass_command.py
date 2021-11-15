import discord
from discord import client
from discord.embeds import *
from discord.ext import commands
import readschedule
from readschedule import nextup, nnextup
from formating import *
from discord_buttons_plugin import *

class Commands(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command(aliases=['next', 'n', 'class', 'c'])
    async def nextclass(self, ctx, arg=None):
        rh = discord.utils.find(lambda r: r.name == 'Mentor: Hanna', ctx.message.guild.roles)
        rd = discord.utils.find(lambda r: r.name == 'Mentor: Don', ctx.message.guild.roles)
        buttons = ButtonsClient(self.client)
        a_ = csvFormater()

        if not arg:

            #next class (has role Mentor: Hanna)
            if rh in ctx.author.roles:
                a_.csvConvert(nextup('hanna'))
                #urel = str(str(a_.url).replace("['", "").replace("']", ""))
                print(a_.start, a_.finish, a_.classroom, a_.teachers, a_.agenda)
                embedVar = discord.Embed(title=a_.subject, color=0x0e41b5)
                embedVar.add_field(name="Tid", value=a_.start, inline=False)  
                embedVar.add_field(name="Slut", value=a_.finish, inline=False)  
                embedVar.add_field(name="Klassrum", value=a_.classroom, inline=False)  
                embedVar.add_field(name="Lärare", value=a_.teachers, inline=False)  
                embedVar.add_field(name="Agenda", value=a_.agenda, inline=False)  
                embedVar.add_field(name="Uppgift", value=a_.assignment, inline=False)   
                print('::', a_.url, '::')
                urel = str(str(str(a_.url).replace("['", "").replace("']", "")).replace("', '","\n"))
                print(';;', urel, ';;')
                if not urel:
                    urel = 'https://thisisbrok.en'
                    print(urel, 'no_url_')
                else:
                    y = 0

                embedVar.add_field(name="Länkar", value=urel, inline=False)
                #embedVar.add_field(name="Länkar", value=urel, inline=False)
                await ctx.send(embed=embedVar)
            
            
            
            #next class (has role Mentor: Don)
            elif rd in ctx.author.roles:
                a_.csvConvert(nextup('don'))
                print(a_.start, a_.finish, a_.classroom, a_.teachers, a_.agenda, a_.url)
                embedVar = discord.Embed(title=a_.subject, color=0x0e41b5)
                embedVar.add_field(name="Tid", value=a_.start, inline=False)
                embedVar.add_field(name="Slut", value=a_.finish, inline=False)  
                embedVar.add_field(name="Klassrum", value=a_.classroom, inline=False)
                embedVar.add_field(name="Lärare", value=a_.teachers, inline=False)
                embedVar.add_field(name="Agenda", value=a_.agenda, inline=False)
                embedVar.add_field(name="Uppgift", value=a_.assignment, inline=False)
                print('::', a_.url, '::')
                urel = str(str(str(a_.url).replace("['", "").replace("']", "")).replace("', '","\n"))
                print(';;', urel, ';;')
                if not urel:
                    urel = 'https://thisisbrok.en'
                    print(urel, 'no_url_')
                else:
                    y = 0

                embedVar.add_field(name="Länkar", value=urel, inline=False)
                await ctx.send(embed=embedVar)


                print("St", a_.start, "StE","e", a_.finish, "ee", "Cl", a_.classroom, "ClE", "Te", a_.teachers, "TeE", "Ag", a_.agenda, "AgE")
        else:

            #.nextclass hanna
            if arg.lower() == 'hanna':
                a_.csvConvert(nextup('hanna'))
                print(a_.start, a_.finish, a_.classroom, a_.teachers, a_.agenda)
                embedVar = discord.Embed(title=a_.subject, color=0x0e41b5)
                embedVar.add_field(name="Tid", value=a_.start, inline=False)  
                embedVar.add_field(name="Slut", value=a_.finish, inline=False)  
                embedVar.add_field(name="Klassrum", value=a_.classroom, inline=False)  
                embedVar.add_field(name="Lärare", value=a_.teachers, inline=False)  
                embedVar.add_field(name="Agenda", value=a_.agenda, inline=False)  
                embedVar.add_field(name="Uppgift", value=a_.assignment, inline=False)  
                print('::', a_.url, '::')
                urel = str(str(str(a_.url).replace("['", "").replace("']", "")).replace("', '","\n"))
                print(';;', urel, ';;')
                if not urel:
                    urel = 'https://thisisbrok.en'
                    print(urel, 'no_url_')
                else:
                    y = 0

                embedVar.add_field(name="Länkar", value=urel, inline=False)
                #urel = str(str(a_.url).replace("['", "").replace("']", ""))
                #embedVar.add_field(name="Länkar", value=urel, inline=False)
                await ctx.send(embed=embedVar)
            #.nextclass don
            elif arg.lower() == 'don':
                a_.csvConvert(nextup('don'))
                print(a_.start, a_.finish, a_.classroom, a_.teachers, a_.agenda)
                embedVar = discord.Embed(title=a_.subject, color=0x0e41b5)
                embedVar.add_field(name="Tid", value=a_.start, inline=False)
                embedVar.add_field(name="Slut", value=a_.finish, inline=False)  
                embedVar.add_field(name="Klassrum", value=a_.classroom, inline=False)
                embedVar.add_field(name="Lärare", value=a_.teachers, inline=False)
                embedVar.add_field(name="Agenda", value=a_.agenda, inline=False)
                embedVar.add_field(name="Uppgift", value=a_.assignment, inline=False)
                print('::', a_.url, '::')
                urel = str(str(str(a_.url).replace("['", "").replace("']", "")).replace("', '","\n"))
                print(';;', urel, ';;')
                if not urel:
                    urel = 'https://thisisbrok.en'
                    print(urel, 'no_url_')
                else:
                    y = 0

                embedVar.add_field(name="Länkar", value=urel, inline=False)
                #urel = str(str(a_.url).replace("['", "").replace("']", ""))
                #embedVar.add_field(name="Länkar", value=urel, inline=False)
                await ctx.send(embed=embedVar)
            
            #Mentor not existing
            else:
                await ctx.send(f'{arg} är ingen mentor. Använd Don eller Hanna!')



def setup(client):
    client.add_cog(Commands(client))
