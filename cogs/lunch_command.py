import discord
from discord import client
from discord.ext import commands
import feedparser
from discord.embeds import Embed

class Commands(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command(aliases=['lunch', 'lu', 'l'])
    async def lun(self, ctx):
        url= "https://skolmaten.se/mediagymnasiet-nacka/rss/days/"
        feed = feedparser.parse(url)
        for post in feed.entries:
            date = "(%d/%02d/%02d)" % (post.published_parsed.tm_year,\
            post.published_parsed.tm_mon, \
            post.published_parsed.tm_mday)
            print("post date: " + date)
            print("post title: " + post.title)
            print("post link: " + post.link)
            print("post content: " + post.description)
        

        embedVar = discord.Embed(title='Lunchen Idag:', color=0x0e41b5)
        embedVar.add_field(name="(kött, fisk, vego)", value=post.description.replace('<br />', '\n'), inline=False)  
        await ctx.send(embed=embedVar)

def setup(client):
    client.add_cog(Commands(client))

