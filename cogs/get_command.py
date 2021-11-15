
import discord
from discord import client
from discord.ext import commands

class Commands(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command(aliases=['g'])
    async def getty(self, ctx):
        log_channel = client.get_channel(LOG_CHANNEL_ID) #LOG CHANNEL

        #Mentor Don
        fileLocation = "./don.ics"
        url1 = 'https://www.schoolity.com/icalendar?id=2fce715d053b1c0f329656e44ca407ff2070f5740f1b0f458d01961bda23a247'

        r = requests.get(url1, allow_redirects=True)
        open(fileLocation, 'wb').write(r.content)

        #Mentor Hanna
        fileLocation = "./hanna.ics"
        url1 = 'https://schoolity.com/icalendar?id=1723311cc4e32826329656e44ca407ff2070f5740f1b0f458d01961bda23a247'

        r = requests.get(url1, allow_redirects=True)
        open(fileLocation, 'wb').write(r.content)

        await log_channel.send('The calendar files has been updated. And will update again in 5 minutes...')

        #Convert
        conv('hanna')
        conv('don')
        await ctx.send('Downloaded new file, please wait up to 2 minutes for file cleaning')


def setup(client):
    client.add_cog(Commands(client))
