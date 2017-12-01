import pymysql
import csv
import pandas as pd
import subprocess
from tkinter import *


#Connection to my Sql
myConnection = pymysql.connect( host="127.0.0.1", user="root", passwd="vikash", db='major_1' )
cursor = myConnection.cursor()
print("sucess")


############################### Firewall###########################################################
infile = R"/home/vikash/PycharmProjects/Major1/TestData/Firewall/Firewall_logs_1.csv"
out=open(infile)
csv_data = csv.reader(out)
for row in csv_data:
    print(row)
    cursor.execute('INSERT INTO firewall(date, time, action, protocol,source_ip, dest_ip, source_port, dest_port, socket_number, acknw) VALUES("%s", "%s","%s", "%s","%s", "%s","%s", "%s","%s", "%s")',row)



myConnection.commit()
cursor.close()
myConnection.close()

#No of requests over the enterprise
input_file = open(infile,"r+")
reader_file = csv.reader(input_file)
value = len(list(reader_file))
print(value)

#Making Dataframes
df= pd.read_csv(infile, usecols=[1,2,4,5], names = ["Date", "Time", "Source", "Destination"] )
#print(df)

firewall_result= df.Source.value_counts()
#List of unique users
print (firewall_result)


#open a GUI Menu
root = Tk()
topFrame= Frame(root)

topFrame.pack()
bottomFrame= Frame(root)
bottomFrame.pack(side=BOTTOM)

button1=Button(bottomFrame,text="Start",fg="green")
button2=Button(bottomFrame,text="Generate Report",fg="blue")
button1.pack(side=LEFT)
button2.pack(side=LEFT)
root.mainloop()