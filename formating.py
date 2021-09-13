import csv
from datetime import timedelta
class csvFormater:
    
    subject = str()

    start = str()
    
    classroom = str()

    teachers = str()

    agenda = str()

    assignment = "Inte implementerad"

    def csvConvert(self, csvTemp):
        csv = csvTemp[11:]
        if len(str(int(csv[0:5].replace(":","")) + 200)) == 3:
            self.start = str(int(csv[0:5].replace(":","")) + 200)[:1] + ":" + str(int(csv[0:5].replace(":","")) + 200)[1:]
        else:
            self.start = str(int(csv[0:5].replace(":","")) + 200)[:2] + ":" + str(int(csv[0:5].replace(":","")) + 200)[2:] 
        if self.start == "":
            self.start = "11:10"
        else:
            y = 0
        print(self.start)
        csv = csv[41:]  
        self.subject = csv[0:csv.find('¤') - 1]
        if self.subject == "":
            self.subject = "None"
        else:
            y = 0
        print(self.subject)
        csv  = csv[csv.find('¤') + 1:]  
        self.teachers = csv[0:csv.find('-') - 1]
        if self.teachers == "?":
            self.teachers = "None"
        else:
            y = 0
        print(self.teachers)
        csv  = csv[csv.find('-') + 2:]  
        self.agenda = csv[0:csv.find('¤')]
        if self.agenda == "":
            self.agenda = "None"
        else:
            y = 0
        print(self.agenda)
        csv = csv[csv.find('¤') + 1:]  
        self.classroom = csv
        if self.classroom == "\n":
            self.classroom = "None"
        else:
            y = 0
        print(self.classroom)
