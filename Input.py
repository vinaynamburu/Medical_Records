from tkinter import filedialog

import pygame
from tkinter import *

root=Tk()
root.minsize(300,300)

l=[]

index=0

def submit1(event):
    global l
    inp1 = inputtxt1.get(1.0, "end-1c")
    inp2 = inputtxt2.get(1.0, "end-1c")
    inp3 = inputtxt3.get(1.0, "end-1c")
    inp4 = inputtxt4.get(1.0, "end-1c")
    inp5 = inputtxt5.get(1.0, "end-1c")
    inp6 = inputtxt6.get(1.0, "end-1c")
    inp7 = inputtxt7.get(1.0, "end-1c")
    inp8 = inputtxt8.get(1.0, "end-1c")
    inp9 = inputtxt9.get(1.0, "end-1c")
    inp10 = inputtxt10.get(1.0, "end-1c")
    inp11 = inputtxt11.get(1.0, "end-1c")
    l.extend((inp1,inp2,inp3,inp4,inp5,inp6,inp7,inp8,inp9,inp10,inp11))
    root.destroy()
    return

label=Label(root,text="Customer_Name")
label.pack()

inputtxt1 = Text(root,height = 1,width = 30)
inputtxt1.pack()

label=Label(root,text="Customer_ID")
label.pack()

inputtxt2 = Text(root,height = 1,width = 30)
inputtxt2.pack()

label=Label(root,text="Customer_Open_Date")
label.pack()

inputtxt3 = Text(root,height = 1,width = 30)
inputtxt3.pack()

label=Label(root,text="Last_Consulted_Date")
label.pack()

inputtxt4 = Text(root,height = 1,width = 30)
inputtxt4.pack()

label=Label(root,text="Vaccination_Type")
label.pack()

inputtxt5 = Text(root,height = 1,width = 30)
inputtxt5.pack()

label=Label(root,text="Doctor_Consulted")
label.pack()

inputtxt6 = Text(root,height = 1,width = 30)
inputtxt6.pack()

label=Label(root,text="State")
label.pack()

inputtxt7 = Text(root,height = 1,width = 30)
inputtxt7.pack()

label=Label(root,text="Country")
label.pack()

inputtxt8 = Text(root,height = 1,width = 30)
inputtxt8.pack()

label=Label(root,text="Post_Code")
label.pack()

inputtxt9 = Text(root,height = 1,width = 30)
inputtxt9.pack()

label=Label(root,text="Date_Of_Birth")
label.pack()

inputtxt10 = Text(root,height = 1,width = 30)
inputtxt10.pack()

label=Label(root,text="Active_Customer")
label.pack()

inputtxt11 = Text(root,height = 1,width = 30)
inputtxt11.pack()

submit=Button(root,text="submit")
submit.pack()

submit.bind("<Button-1>",submit1)

root.mainloop()

import sqlite3
from sqlite3.dbapi2 import Cursor

connection = sqlite3.connect('Records.db')

cursor = connection.cursor()

Table = """CREATE TABLE IF NOT EXISTS Details(Customer_Name VARCHAR(255),Customer_ID VARCHAR(18),Customer_Open_Date DATE,Last_Consulted_Date DATE,Vaccination_Type CHAR(5),Doctor_Consulted CHAR(255),State CHAR(5),Country CHAR(5),Post_Code INTEGER,Date_Of_Birth DATE,Active_Customer CHAR(1))"""

cursor.execute(Table)

table_rows = [(l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7],l[8],l[9],l[10])]

sql_statement = 'INSERT INTO Details VALUES (?,?,?,?,?,?,?,?,?,?,?)'

cursor.executemany(sql_statement, table_rows)

cursor.execute("SELECT * FROM Details")

results = cursor.fetchall()
print(results)
connection.commit()
connection.close()
