import sys
from datetime import datetime, timedelta
import csv
import re




def cleanCSV(s):
    now = datetime.now()
    tentoclass = now + timedelta(hours=-2)
    current_time = tentoclass.strftime("%m%d%H")
    with open('%s.csv'% s , 'r+') as g:    
        firstline1 = g.readline()[4:]
        firstline2 = firstline1[0:9]
        #print(firstline2)
        x = re.findall("[a-z]", firstline2)

        if firstline2 == "t,End,Sum":
            data = g.read()
            g.seek(0)
            g.write(data)
            g.truncate()
        elif x:
            data = g.read()
            g.seek(0)
            g.write(data)
            g.truncate()

        else:
            fl3 = firstline2.replace(" ", "")
            fl4 = fl3.replace("-", "")
            if fl4 < current_time:
                data = g.read()
                g.seek(0)
                g.write(data)
                g.truncate()
            else:
                return

'''
def cleanCSV(s):
    now = datetime.now()
    tentoclass = now + timedelta(hours=-2)
    current_time = tentoclass.strftime("%m%d%H")
    with open('%s.csv'% s , 'r') as g:
        csv_reader = csv.reader(g, delimiter=',')
        for row in csv_reader:
            q = row[5:][:-12]
            r = q.replace(" ", "") 
            o = r.replace("-", "")
            print(o)
            if o < current_time:
                with open('%s.csv'% s , 'r+') as f:
                    firstLine = f.readline()
                    data = f.read()
                    f.seek(0)
                    f.write(data)
                    f.truncate()
                    return firstLine
'''
def compTime(s):
    try: 
        now = datetime.now()
        tentoclass = now + timedelta(hours=-2, minutes=-10) #sets the 
        current_time = tentoclass.strftime("%Y-%m-%d %H:%M:%s+00:00") #formats as YYYY-mm-dd HH:MM:SS+00:00
        with open('%s.csv' % s , 'r') as f: #open csv to f
            csv_reader = csv.reader(f, delimiter=',') #load f as csv into csv_reader set delim to ,
            for row in csv_reader: #for every row of the csv do
                if row[0][:-8] == current_time[:-8]: #if minutes match do
                    #clint = (row[0][:-8]),(row[1]),(row[2]),(row[3]),(row[4]) #sets clint (ClassINTen)
                    #return clint #returns all rows
                    #sleep(1200)
                    with open('%s.csv' % s , 'r+') as f: # open file in read / write mode
                        firstLine = f.readline() # read the first line and throw it out
                        data = f.read() # read the rest
                        f.seek(0) # set the cursor to the top of the file
                        f.write(data) # write the data back
                        f.truncate() # set the file size to the current size
#                        print(firstLine)
                        return firstLine
                        cleanCSV('%s')
                else:
                    #print((row[0]),"no") #sends no otherwise
                    #print(now, "CURRENT") #prints the current time
                    do = 0 #just do something man
 #                   print(current_time[:-8])
    except Exception as e:
        a = 'o'
        #print(f'Error: {e}', 'TBACK')
def nextup(s):
    with open('%s.csv'% s, 'r') as h:
       # h.seek(2)
        nextclass = h.readline()
        h.seek(0)
        return nextclass

def nnextup(s):
    with open('%s.csv'% s, 'r') as m:
        nesdf = m.read().split('\n')[1]
        return nesdf

#compTime("don")
#print(compTime("don"))
#for i in range(60):
#    print(compTime("don"))
