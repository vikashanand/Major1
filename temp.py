import pandas as pd
import csv
class Apache():
    def apache_analysis(self):
        infile = "/home/vikash/PycharmProjects/Major/Major1/TestData/Apache/logs.csv"
        df_apache = pd.read_csv(infile, usecols=[1, 2, 3,6],
                         names=["Source", "Date", "Time", "Status"])
        print("**********lable:Class Apache\n", df_apache)

Ap=Apache()
Ap.apache_analysis()