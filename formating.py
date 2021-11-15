import csv
from datetime import timedelta
class csvFormater:
    
    subject = str()

    start = str()

    finish = str()

    classroom = str()

    teachers = str()

    agenda = str()

    assignment = "Inte implementerad"

    url = str()

    def csvConvert(self, csvTemp):
        csv = csvTemp[11:]
        if len(str(int(csv[0:5].replace(":","")) + 100)) == 3:
            self.start = str(int(csv[0:5].replace(":","")) + 100)[:1] + ":" + str(int(csv[0:5].replace(":","")) + 100)[1:]
        else:
            self.start = str(int(csv[0:5].replace(":","")) + 100)[:2] + ":" + str(int(csv[0:5].replace(":","")) + 100)[2:] 
        if self.start == "":
            self.start = "11:10"
        else:
            y = 0
        print(self.start)

        csv = csvTemp[37:]
        if len(str(int(csv[0:5].replace(":","")) + 100)) == 3:
            self.finish = str(int(csv[0:5].replace(":","")) + 100)[:1] + ":" + str(int(csv[0:5].replace(":","")) + 100)[1:]
        else:
            self.finish = str(int(csv[0:5].replace(":","")) + 100)[:2] + ":" + str(int(csv[0:5].replace(":","")) + 100)[2:]
        if self.finish == "":
            self.finish = "11:40"
        else:
            y = 0
        print(self.finish)

        csv = csvTemp[52:]  
        self.subject = csv[0:csv.find('¤')]
        if self.subject == "":
            self.subject = "None_w"
            print('ERROR: subject not found or not valid. sub:', self.subject, ':subend')
        else:
            y = 0
        print(self.subject, y)
        csv  = csv[csv.find('¤') + 1:]  
        self.teachers = csv[0:csv.find('-') - 1]
        if self.teachers == "?":
            self.teachers = "None_w"
            print('ERROR: teachers not found or not valid. tch:', self.teachers, ':tchend')
        else:
            y = 0
        print(self.teachers, y)
        csv  = csv[csv.find('-') + 2:]  
        self.agenda = csv[0:csv.find('¤')]
        if self.agenda == "":
            self.agenda = "None_w"
            print('ERROR: agenda not found or not valid. agd:', self.agenda, ':agdend')
        else:
            y = 0
        print(self.agenda)
       
        csv = csv[csv.find('¤') + 1:]  
        self.classroom, sep, tail = csv.partition('¤')
        if self.classroom == "":
            self.classroom = "None_w"
            print('ERROR: classroom not found or not valid. crm:', self.classroom, ':crmend')
        else:
            y = 0
        print(self.classroom)
        csv = csv[csv.find('¤') + 1:]
        self.url = csv
        if self.url == "\n":
            self.url = ['https://www.schoolity.com']
            print('ERROR: url not found or not valid. url:', self.url, ':urlend')
        else:
            y = 0

