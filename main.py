#Importing stuff
from readschedule import *
from ical2csv import *
from config import *
import discord
import requests
import os
from formating import *
from discord.ext import commands, tasks
from comp import *

#Command prefix
client = commands.Bot(command_prefix = '.')
print("set prefix")
#Update calender file
@tasks.loop(minutes=5)
async def update():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you fail class"))
    await client.wait_until_ready()
    log_channel = client.get_channel(LOG_CHANNEL_ID) #LOG CHANNEL
    print("updated file")
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

'''
@tasks.loop(seconds=0.1)
async def clen():
    cleanCSV('hanna')
    cleanCSV('don')
    print("bruh")
'''

#Read files
@tasks.loop(seconds=0.1)
async def read():
    await client.wait_until_ready()
    
    #CleanCSV
    cleanCSV('hanna')
    cleanCSV('don')
    
    currentClassH = compTime('hanna')
    currentClassD = compTime('don')
    print(currentClassD)

    if currentClassH == currentClassD:
        #Send one
        #print('one')
        y = 0 
    else:
        #Send two
        #print('two')
        y = 1
#Cogs (Loading commands)
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
        print("loaded cogs")

@tasks.loop(minutes=1)
async def comp():
    await client.wait_until_ready()
    compclass('don')
    compclass('hanna')
    
print("attempting to execute client.run")
i = client.run(TOKEN)
print(i)
