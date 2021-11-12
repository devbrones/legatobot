def compTime(s):
 26     try:
 25         now = datetime.now()
 24         tentoclass = now + timedelta(hours=-2, minutes=-10) #sets the
 23         current_time = tentoclass.strftime("%Y-%m-%d %H:%M:%s+00:00") #formats as YYYY-mm-dd HH:MM:SS+00:00
 22         with open('%s.csv' % s , 'r') as f: #open csv to f
 21             csv_reader = csv.reader(f, delimiter=',') #load f as csv into csv_reader set delim to ,
 20             for row in csv_reader: #for every row of the csv do
 19                 if row[0][:-8] == current_time[:-8]: #if minutes match do
 15                     with open('%s.csv' % s , 'r+') as f: # open file in read / write mode
 14                         firstLine = f.readline() # read the first line and throw it out
 13                         data = f.read() # read the rest
 12                         f.seek(0) # set the cursor to the top of the file
 11                         f.write(data) # write the data back
 10                         f.truncate() # set the file size to the current size
  8                         return firstLine
  7                         cleanCSV('%s')
  6                 else:
  3                     do = 0 #just do something man
