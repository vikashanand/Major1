import pymysql

myConnection = pymysql.connect( host="127.0.0.1", user="root", passwd="vikash", db='sys' )
#doQuery( myConnection )
print("sucess")
myConnection.close()

infile = R"/home/vikash/PycharmProjects/Major1/TestData/Firewall_logs.txt"

important = []

with open(infile) as f:
    f = f.readlines()

for line in f:
    important.append(line)

print(important)

