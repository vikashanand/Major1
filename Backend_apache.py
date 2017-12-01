import pymysql
import csv
import pandas as pd

#Connection
myConnection = pymysql.connect( host="127.0.0.1", user="root", passwd="vikash", db='major_1' )
cursor = myConnection.cursor()
print("sucess")


