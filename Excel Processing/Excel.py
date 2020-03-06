#Keaton Smith
#3/6/2020

#This program allows the user to import an ACT file and check what fields could be handled by webservices and which need
#to be keyed in by data entry. Additionally the user can select which columns webservices is capable of processing.

import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import pandas as pd

root= tk.Tk()
root.title("Process Excel")

canvas1 = tk.Canvas(root, width = 300, height = 300, bg = 'lightsteelblue')
canvas1.pack()

#The default columns being checked for.
disqualifying_fields = ['14', '23', '25', '47', '65', '66', '67']

#For the grid of check boxes the user can use to select columns.
rows=10
columns=10
boxes = []
boxVars = []

#Determines which boxes have been checked.
def getSelected():
    selected = []
    for i in range(len(boxVars)):
        for j in range(len(boxVars[i])):
            if boxVars[i][j].get() == 1:
                selected.append(i * 10 + j + 1)
    #Updates the global disqualifying_fields list with the new values.
    disqualifying_fields.clear()
    for bad in selected:
        disqualifying_fields.append(str(bad))


#Opens a dialog to select the excel file and then does the checks.
def getExcel ():
    global df

    #This will hold the message for the info dialog at the end.
    text = []
    import_file_path = filedialog.askopenfilename()
    df = pd.read_excel (import_file_path)
    #Joins the elements of disqualifying_fields into one string for checks.
    pattern = '|'.join(disqualifying_fields)
    #Pulls out the addition and termination updates.
    num_adds = df.loc[df['Update Type'] == 'A']
    num_terms = df.loc[df['Update Type'] == 'T']
    total_entries = len(df.index)
    adds = len(num_adds.index)
    terms = len(num_terms.index)
    text.append("Number of addition updates: " + str(adds))
    text.append("Number of termination updates: " + str(terms))
    non_web_entries = len(num_adds.index)
    #Removes the addition and termination updates. Only change updates should be left.
    df = df[df['Update Type'] != 'A']
    df = df[df['Update Type'] != 'T']
    #Look for rows with updates to disqualifying columns.
    df = df[df['Enhanced ACT Indicator'].astype(str).str.contains(pattern)]
    changes = len(df.index)
    #Show the user the result.
    text.append("Number of non-Webservice changes: " + str(changes))
    text.append("Total number of Non-Webservice entries: " + str(adds + changes))
    text.append("******************")
    goods = total_entries - adds - changes
    text.append("Number of records webservice can handle: " + str(goods))
    text.append("Percentage of Total Records: " + str((goods / total_entries) * 100) + "%")
    messagebox.showinfo("Result", "\n".join(text))

#Present the user with a new window where they can change which fields are disqualifying.
def changeFields ():
    #Open a new window.
    window = tk.Toplevel(root)
    boxVars.clear()
    boxes.clear()

    #Create a 2D array to hold the checkboxes.
    for i in range(rows):
        boxVars.append([])
        for j in range(columns):
            boxVars[i].append(IntVar())
            boxVars[i][j].set(0)

    #Fill the 2D array with checkboxes and postion them on the screen.
    for x in range(rows):
        boxes.append([])
        for y in range(columns):
            Label(window, text= "Select Which Columns Webservices Can't Handle").grid(row=0, column=3, columnspan=7)
            boxes[x].append(Checkbutton(window, variable = boxVars[x][y], text = str(x * 10 + y + 1)))
            boxes[x][y].grid(row=x+1, column=y+1)

    #Pre-check any boxes that appear in disqualifying_fields.
    for checked in disqualifying_fields:
        num = int(checked)
        if num % 10 == 0:
            boxes[int((num / 10) - 1)][int((num % 10) - 1)].select()
        else:
            boxes[int(num / 10)][int((num % 10) - 1)].select()

    #Add the buttons to go back and to save the new values.
    goBackButton = tk.Button(window, text='Go Back', command=window.wm_iconify, bg='red', fg='white', font=('helvetica', 12, 'bold'))
    goBackButton.grid(row = 12, column = 6, columnspan = 3)
    saveButton = tk.Button(window, text='Save', command=getSelected, bg='green', fg='white', font=('helvetica', 12, 'bold'))
    saveButton.grid(row = 12, column = 3, columnspan = 3)
    

#Add the three buttons to the main screen to change fields, load an excel, and quit.
browseButton_Excel = tk.Button(text='Import Excel File', command=getExcel, bg='green', fg='white', font=('helvetica', 12, 'bold'))
quitButton = tk.Button(text='QUIT', bg='red', fg='white', font=('helvetica', 12, 'bold'), command=root.destroy)
changeFieldsButton = tk.Button(text='Modify Acceptable Fields', bg='blue', fg='white', font=('helvetica', 12, 'bold'), command=changeFields)
canvas1.create_window(150, 150, window=browseButton_Excel)
canvas1.create_window(150, 250, window=quitButton)
canvas1.create_window(150, 50, window=changeFieldsButton)

#Calls the main loop.
root.mainloop()

