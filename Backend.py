import pymysql
import csv
import pandas as pd

#Connection to my Sql
myConnection = pymysql.connect( host="127.0.0.1", user="root", passwd="vikash", db='major_1' )
cursor = myConnection.cursor()
print("sucess")



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
print(df)

#List of unique users
print (df.Source.value_counts())



