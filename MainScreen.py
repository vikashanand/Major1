from tkinter import *

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