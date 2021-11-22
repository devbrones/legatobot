
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
        print(f'Error: {e}', 'TBACK')
