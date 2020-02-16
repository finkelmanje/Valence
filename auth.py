from tkinter import *
from datetime import datetime
import time
from time import sleep
import os
import glob
import Pmw

from tkinter import ttk

class Journal():
    def __init__(self, root):


        # Tab manager
        self.tabLogic = ttk.Notebook(window)
        self.tab1 = ttk.Frame(tabLogic)
        self.tab2 = ttk.Frame(tabLogic)
        self.tab3 = ttk.Frame(tabLogic)
        self.tabLogic.add(self.tab1, text = 'Write')
        self.tabLogic.add(self.tab2, text = 'Read')
        self.tabLogic.add(self.tab3, text = 'Display')


        # Writing tab
        textEntry = Text(tab1, height = 30, width = 135)
        textEntry.pack()
        textEntry.insert(END, "")
        textEntry.grid(column = 0, row = 0, ipady = 10)

        # Writing button framework
        diaryWriteButton = Button(tab1, text = "Submit", command = submit)
        diaryWriteButton.grid(column = 0, row = 1, pady = 10)

        # --------------------------------------------------------


        # Creating a sorted list of text files from the directory
        dir = os.path.dirname(os.path.abspath(__file__))
        filename = os.path.join(dir, '*.txt')
        clean_filename = os.path.basename(filename)
        entry_list = glob.glob(clean_filename)
        entry_list.sort(reverse = True)

        # Dropdown menu logic
        dropdownSetting = StringVar(window)
        dropdownSetting.set('Journal Entries') # TODO: make sure that 'Journal Entries' isn't an accepted string
        readFileSelection = 'README.txt'


        # Selecting option from dropdown menu
        popupMenu = OptionMenu(tab2, dropdownSetting, *entry_list)
        Label(tab2, text = "Choose an entry").grid(row = 1, column = 1, padx = 416, pady = 5)
        diaryReadButton = Button(tab2, text = 'Open', command = readFile)
        diaryReadButton.grid(row = 3, column = 1)
        popupMenu.grid(row = 2, column = 1)



        # Reading tab
        textReading = Text(tab2, height = 30, width = 108)
        textReading.grid(column = 1, row = 6, pady = 10)
        filename = readFileSelection
        textReading.insert('end', open(filename,'r').read())




        # ------------------------------------------------------------------
        # Data display tab
        label = Label(tab3, text = "dataDisplay")
        label.grid(column = 0, row = 0)
        tabLogic.pack(expand = 1, fill = 'both')

    # Writing button logic
    def submit(self):
        curr_time = datetime.now()
        date_time = curr_time.strftime("%c")
        input = self.textEntry.get("1.0", 'end-1c')
        if not len(input) == 0:
            with open(date_time + '.txt', 'w') as file:
                file.write(input)
            self.diaryWriteButton.configure(text = "Submitted!")
            self.newEntryButton = Button(tab1, text="New Entry", command=newEntry)
            self.newEntryButton.grid(column=0, row=2, pady=10)

    def newEntry(self):
        self.textEntry.delete(1.0, END)
        self.diaryWriteButton.configure(text = "Submit")
        self.grid_forget()

    def readFile(self): # TODO: implement readFile
        if dropdownSetting.get() != 'Journal Entries':
            readFileSelection = dropdownSetting.get()
            filename = readFileSelection
            self.textReading.delete(1.0,END)
            self.textReading.insert('end', open(filename, 'r').read())

# Window setup
window = Tk()
window.geometry("1008x630+336+210")
mainframe = Frame(window)
window.title("Journal")
window.mainloop()
