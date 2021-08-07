from tkinter import filedialog

import pygame
from tkinter import *

root=Tk()
root.minsize(300,300)

def submit1(event):
    global value
    value = inputtxt1.get(1.0, "end-1c")
    root.destroy()
    
label=Label(root,text="Customer_Name")
label.pack()

inputtxt1 = Text(root,height = 1,width = 30)
inputtxt1.pack()


submit=Button(root,text="submit")
submit.pack()

submit.bind("<Button-1>",submit1)

root.mainloop()

import sqlite3
from sqlite3.dbapi2 import Cursor

connection = sqlite3.connect('Records.db')

cursor = connection.cursor()

cursor.execute('SELECT * FROM Details where Customer_Name = ?',(value,))

results = cursor.fetchall()

root=Tk()
root.minsize(300,300)

def submit1(event):
    root.destroy()
    return

label=Label(root,text="Customer_Name is "+str(results[0][0]))
label.pack()

label=Label(root,text="Customer_ID is "+str(results[0][1]))
label.pack()

label=Label(root,text="Customer_Open_Date is "+str(results[0][2]))
label.pack()

label=Label(root,text="Last_Consulted_Date is "+str(results[0][3]))
label.pack()

label=Label(root,text="Vaccination_Type is "+str(results[0][4]))
label.pack()

label=Label(root,text="Doctor_Consulted is "+str(results[0][5]))
label.pack()

label=Label(root,text="State is "+str(results[0][6]))
label.pack()

label=Label(root,text="Country is "+str(results[0][7]))
label.pack()

label=Label(root,text="Post_COde is "+str(results[0][8]))
label.pack()

label=Label(root,text="Date_Of_Birth is "+str(results[0][9]))
label.pack()

label=Label(root,text="Active_Customer is "+str(results[0][10]))
label.pack()

submit=Button(root,text="Close")
submit.pack()

submit.bind("<Button-1>",submit1)

root.mainloop()
