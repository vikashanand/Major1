import matplotlib
matplotlib.use("TkAgg")

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

import tkinter as tk
import numpy as np
import pymysql
import csv
import pandas as pd
from pandastable import Table, TableModel

#Default variable used for Font
LARGE_FONT=("Verdana",15)
MID_FONT=("Verdana",13)


class SIEM_Demo(tk.Tk):

    # Initialisation of parameters
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container= tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight= 1)
        container.grid_columnconfigure(0, weight=1)

        self.frame = {}

        for F in (StartPage, PageFirewall, PageApache, PageFirewallActiveUser, PageEnterpriseApplication):
            frame= F(container, self)

            self.frame[F]= frame

            frame.grid(row=0,column=0,sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame =self.frame[cont]
        frame.tkraise()



class StartPage(tk.Frame):

    # Initialisation of parameters
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        lable =tk.Label(self, text="Start Page", font=LARGE_FONT)
        lable.pack(pady=10, padx=10)

        button1= tk.Button(self, text="Firewall", command= lambda: controller.show_frame(PageFirewall))
        button1.pack(pady=25, padx=10)

        button2 = tk.Button(self, text="Apache Server", command=lambda: controller.show_frame(PageApache))
        button2.pack(pady=40, padx=10)

        button3= tk.Button(self ,text="Enterprise Application", command= lambda:controller.show_frame(PageEnterpriseApplication))
        button3.pack(pady=55, padx=10)


#------- End of Start Page Class --------------------------


class PageFirewall(tk.Frame):

    #Initialisation of parameters
    def __init__(self,parent, controller):
        tk.Frame.__init__(self, parent)
        lable = tk.Label(self, text="Firewall", font=LARGE_FONT)
        lable.pack(pady=10, padx=10)

        objPF= Firewall()
        dfPF=objPF.failed_attempt()
        print("-------------Screen UI ---",dfPF)

        lable1 = tk.Label(self, text="Firewall Unauthorised Access", font=LARGE_FONT)
        lable1.pack(pady=20, padx=10)
        f=tk.Frame(self)
        f.pack(pady=12, padx=5,expand=False)
        pt=Table(f,dataframe=dfPF,showstatusbar=True, showtoolbar=False)
        pt.show()

        button2 = tk.Button(self, text="Traffic", command=lambda: controller.show_frame(PageFirewallActiveUser))
        button2.pack()

        button1 = tk.Button(self, text="Back", command=lambda: controller.show_frame(StartPage))
        button1.pack()



#--------------- End of Firewall Page---------------------


class PageApache(tk.Frame):

    # Initialization Function
    def __init__(self,parent, controller):
        tk.Frame.__init__(self, parent)
        lable = tk.Label(self, text="Apache Server", font=LARGE_FONT)
        lable.grid(row=0, column=1)

        button1 = tk.Button(self, text="Back", command=lambda: controller.show_frame(StartPage))
        button1.grid(row=3, column=1)
        # Object of Apache Class
        print("-----------PageApapche-------")
        obj_ap = Apache_Server()
        apache_df = obj_ap.apache_analysis()
        print(apache_df)
        lb1=tk.Label(self,text="Sucessfull Attempts",font=MID_FONT)
        lb1.grid(row=1, column=0)
        f = tk.Frame(self)
        f.grid(row=2, column=0)
        pt_apache_active = Table(f, dataframe=apache_df, showstatusbar=True, showtoolbar=False)
        pt_apache_active.show()

        apache_df_fail=obj_ap.apache_failed()
        lb2 = tk.Label(self, text="Failed Attempts",font=MID_FONT)
        lb2.grid(row=1, column=2)
        g=tk.Frame(self)
        g.grid(row=2, column=2)
        pt_apache_fail=Table(g,dataframe=apache_df_fail,showstatusbar=True, showtoolbar=False)
        pt_apache_fail.show()



class PageFirewallActiveUser(tk.Frame):
    def __init__(self,parent, controller):
        tk.Frame.__init__(self, parent)
        lable = tk.Label(self, text="Active Users", font=LARGE_FONT)
        lable.pack(pady=10, padx=10)

        print("---------------------------------------Hello")

        button1 = tk.Button(self, text="Back", command=lambda: controller.show_frame(StartPage))
        button1.pack()

        #Code for firewall class
        fw=Firewall()
        f_data=fw.firewall_analysis()
        print("***********Flag1")
        #f_data.columns=['IP', 'Attempts']

        print(f_data,"\n",f_data.columns)

        #x=[1,2,3,4,5,6,7,8,9]
        l=len(f_data.index)
        print("\n**************",l)
        x = range(1,l)
        print(x)

        f= Figure(figsize=(5,5), dpi=70)
        a= f.add_subplot(111)
        y=f_data[0:]
        print("********************lable 3", y)
        ind= np.arange(l)
        width=.4

        rects1=a.bar(ind,y,width)
        canvas=FigureCanvasTkAgg(f,self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.TOP,fill=tk.BOTH, expand=True)

#------------------------ end of PageFirewall_ActiveUsers------------------


class PageEnterpriseApplication(tk.Frame):

    #Inisialization Function
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        lable = tk.Label(self, text="Enterprise Application", font=LARGE_FONT)
        lable.grid(row=0, column=1)


        button1 = tk.Button(self, text="Back", command=lambda: controller.show_frame(StartPage))
        button1.grid(row=3, column=1)


        obj_Enter = EnterpriseApplication()
        enterApp_df = obj_Enter.enterprise_analysis()
        print(enterApp_df)

        lb1 = tk.Label(self, text="Sucessfull Attempts", font=MID_FONT)
        lb1.grid(row=1, column=0)

        f = tk.Frame(self)
        f.grid(row=2, column=0)
        pt_enterprise_active = Table(f, dataframe=enterApp_df, showstatusbar=True, showtoolbar=False)
        pt_enterprise_active.show()

        enterApp_df_fail = obj_Enter.enterprise_fail()

        lb2 = tk.Label(self, text="Failed Attempts",font=MID_FONT)
        lb2.grid(row=1, column=2)

        g = tk.Frame(self)
        g.grid(row=2, column=2)
        pt_apache_fail = Table(g, dataframe=enterApp_df_fail, showstatusbar=True, showtoolbar=False)
        pt_apache_fail.show()

class Firewall():

    def firewall_analysis(self):

        myConnection = pymysql.connect(host="127.0.0.1", user="root", passwd="vikash", db='major_1')
        cursor = myConnection.cursor()
        print("sucess")

        infile = "/home/vikash/PycharmProjects/Major1/TestData/Firewall/Firewall_logs_1.csv"
        out = open(infile)
        csv_data = csv.reader(out)
        for row in csv_data:
            #print(row)
            cursor.execute(
                'INSERT INTO firewall(date, time, action, protocol,source_ip, dest_ip, source_port, dest_port, socket_number, acknw) VALUES("%s", "%s","%s", "%s","%s", "%s","%s", "%s","%s", "%s")',
                row)

        myConnection.commit()
        cursor.close()
        myConnection.close()

        # No of requests over the enterprise
        input_file = open(infile, "r+")
        reader_file = csv.reader(input_file)
        value = len(list(reader_file))
        print(value)

        # Making Dataframes
        df = pd.read_csv(infile, usecols=[1, 2, 4, 5,7,8], names=["Date", "Time", "Source", "Destination","Source Port", "Dest. Port"])
        print("**********lable:Class Firewall",df)

        df_fail = df.loc[df['Source Port'] == '-']
        print("**********lable:Class Firewall_ Failed method ", df_fail)


        firewall_result = df.Source.value_counts()
        firewall_result.columns=["IP", "Attempts"]
        # List of unique users
        print(firewall_result)

        return firewall_result


    def failed_attempt(self):
        infile = R"/home/vikash/PycharmProjects/Major/Major1/TestData/Firewall/Firewall_logs_1.csv"
        df = pd.read_csv(infile, usecols=[1, 2, 4, 5, 7, 8],
                         names=["Date", "Time", "Source", "Destination", "Source Port", "Dest. Port"])
        print("**********lable:Class Firewall", df)

        df_fail = df.loc[df['Source Port'] == '-']
        print("**********lable:Class Firewall_ Failed method ", df_fail)
        return df_fail



class Apache_Server():

    # Function definition
    def apache_analysis(self):
        print("////////////////////Apache Class///////////")
        infile = "/home/vikash/PycharmProjects/Major/Major1/TestData/Apache/logs.csv"
        df_apache = pd.read_csv(infile, usecols=[0, 1, 2, 5], names=["Source IP", "Date", "Time", "Status"])
        print("**********lable:Class Apache", df_apache)
        df_apache_1=df_apache.loc[df_apache["Status"] == 200]
        df_apache_2=df_apache_1.drop("Status",1) # 0 Row 1 column
        return df_apache_2

    # Function definition
    def apache_failed(self):
        infile = "/home/vikash/PycharmProjects/Major/Major1/TestData/Apache/logs.csv"
        df_apache = pd.read_csv(infile, usecols=[0, 1, 2, 5], names=["Source IP", "Date", "Time", "Status"])
        df_fail = df_apache.loc[df_apache["Status"] != 200]
        df_fail_1=df_fail.drop("Status",1) # 0 Row 1 column
        return df_fail_1;

#------------------ End of Apache Server class -------------


class EnterpriseApplication():

    #Function definition
    def enterprise_analysis(self):
        infile = "/home/vikash/PycharmProjects/Major/Major1/TestData/Enterprise/Enter_logs.csv"
        df_enterprise=pd.read_csv(infile, usecols=[0, 1, 2, 5], names=["Source", "Date", "Time", "Status"])
        df_enterprise_1=df_enterprise.loc[df_enterprise["Status"] == 100]
        return df_enterprise_1

    #FUnction Definition
    def enterprise_fail(self):
        infile = "/home/vikash/PycharmProjects/Major/Major1/TestData/Enterprise/Enter_logs.csv"
        df_enterprise_f = pd.read_csv(infile, usecols=[0, 1, 2, 5], names=["Source", "Date", "Time", "Status"])
        df_enterprise_1_f = df_enterprise_f.loc[df_enterprise_f["Status"] != 100]
        return df_enterprise_1_f

#--------------------------end of Enterprise Application Class-----


app = SIEM_Demo()
app.mainloop()