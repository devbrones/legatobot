import sys
import os.path
from icalendar import Calendar
import csv


def conv(s):
    filename = '%s.ics' % s
# TODO: use regex to get file extension (chars after last period), in case it's not exactly 3 chars.
    file_extension = str(filename)[-3:]
    headers = ('Start', 'End', 'Summary', 'Description', 'Location', 'Url')

    class CalendarEvent:
        """Calendar event class"""
        start = ''
        end = ''
        summary = ''
        description = ''
        location = ''
        url = ''

        def __init__(self, name):
            self.name = name

    events = []


    def open_cal():
        if os.path.isfile(filename):
            if file_extension == 'ics':
                print("Extracting events from file:", filename, "\n")
                f = open(filename, 'rb')
                gcal = Calendar.from_ical(f.read())

                for component in gcal.walk():
                    event = CalendarEvent("event")
                    if component.get('TRANSP') == 'TRANSPARENT': continue #skip event that have not been accepted
                    if hasattr(component.get('dtstart'), 'dt'):
                        event.start = component.get('dtstart').dt
                    if hasattr(component.get('dtend'), 'dt'):
                        event.end = component.get('dtend').dt
                    if component.get('SUMMARY') == None: continue #skip blank items
                    event.summary = component.get('SUMMARY')
                    if component.get('DESCRIPTION') == None: continue #skip blank items
                    event.description = component.get('DESCRIPTION')
                    event.location = component.get('LOCATION')
                    event.url = component.get('URL')

                    events.append(event)
                f.close()
            else:
                print("You entered ", filename, ". ")
                print(file_extension.upper(), " is not a valid file format. Looking for an ICS file.")
                exit(0)
        else:
            print("I can't find the file ", filename, ".")
            print("Please enter an ics file located in the same folder as this script.")
            exit(0)


    def csv_write(icsfile):
        sortedevents=sorted(events, key=lambda obj: obj.start)
        csvfile = icsfile[:-3] + "csv"
        try:
            with open(csvfile, 'w') as myfile:
                wr = csv.writer(myfile, delimiter='¤')
                wr.writerow(headers)
                for event in sortedevents:
                    values = (event.start, event.end, event.summary.encode('utf8').decode(), event.description.encode('utf8').decode(), event.location, event.url)
                    wr.writerow(values)
                print("Wrote to ", csvfile, "\n")
        except IOError:
            print("Could not open file! Please close Excel!")
            exit(0)


    def debug_event(class_name):
        print("Contents of ", class_name.name, ":")
        print(class_name.summary)
        print(class_name.description)
        print(class_name.location)
        print(class_name.start)
        print(class_name.end)
        print(class_name.url)

    open_cal()
    csv_write(filename)
