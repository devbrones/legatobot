import requests
import json

botToken = "ODc5NjcyNDA2NjE5MzI0NDU2.YSTIxQ.0bynWydGwnLRuyInCf7djsTTDIs"

headers = {"Authorization":"Bot {}".format(botToken),
           "User-Agent":"Legatobot (python, version balls)",
           "Content-Type":"application/json", }

def getListedEvents(guildid):
    r = requests.get('https://discordapp.com/api/guilds/' + guildid + '/scheduled-events', headers = headers)
    if (r.status_code == "200"):
        return r.json()
    else:
        print("Error, api not responding (getguildevents)")
        return "ERROR"

def createEvent(guildid, clArr):
    subject = clArr[4] + " - " + clArr[0]
    start = clArr[1]
    finish = clArr[2]
    classroom = clArr[3]
    agenda = clArr[5]
    
    ## {"name":"Svenska 1 - Hanna åberg","description":"test","privacy_level":2,"scheduled_start_time":"2021-11-22T19:00:00.516Z","scheduled_end_time":"2021-11-22T21:00:00.516Z","entity_type":3,"channel_id":null,"entity_metadata":{"location":"211"}}


    payload = {"name":subject,"description":agenda,"privacy_level":2,"scheduled_start_time":start, "scheduled_end_time":finish,"entity_type":3,"entity_metadata":{"location":classroom}}
    r = requests.post("https://discordapp.com/api/guilds/{}/scheduled-events".format(guildid), headers=headers, data=json.dumps(payload))
    print (r.text)
    print (r.status_code)


