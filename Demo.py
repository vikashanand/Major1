import sys
import pymysql
import csv
import pandas as pd
import matplotlib as plt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QGridLayout
from matplotlib import figure
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas


class firewall():
    def firewall_analysis(self):
        myConnection = pymysql.connect(host="127.0.0.1", user="root", passwd="vikash", db='major_1')
        cursor = myConnection.cursor()
        print("sucess")

        infile = R"/home/vikash/PycharmProjects/Major1/TestData/Firewall/Firewall_logs_1.csv"
        out = open(infile)
        csv_data = csv.reader(out)
        for row in csv_data:
            print(row)
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
        df = pd.read_csv(infile, usecols=[1, 2, 4, 5], names=["Date", "Time", "Source", "Destination"])
        # print(df)

        firewall_result = df.Source.value_counts()
        # List of unique users
        print(firewall_result)
        return firewall_result


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'S I E M'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create Grid Layout
        grid = QGridLayout()
        self.setLayout(grid)


        # FireWall Buttons
        buttonFirewall = QPushButton('Firewall', self)
        buttonFirewall.clicked.connect(self.clickFirewall)  # functionality added to  button
        buttonFirewall.setToolTip('Press this button for starting the application')
        # buttonFirewall.move(100,430)

        grid.addWidget(buttonFirewall, 2, 0)

        self.show()

    def clickFirewall(self):
        print('*****Clicked Firewall button.*******')
        demoObj = firewall()
        dataFirewall = demoObj.firewall_analysis()
        print("DataFrame : ", dataFirewall)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
