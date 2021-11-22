import requests


def getListedEvents(guildid):
    r = requests.get('https://discord.com/api/guilds/' + guildid + '/scheduled-events')
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
    payload = {"entity_metadata" : {"location":classroom}, "name" : subject, "privacy_level" : "2", "scheduled_start_time" : start, "scheduled_end_time" : finish, "description" : agenda, "entity_type" : "3"}



