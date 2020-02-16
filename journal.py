from tkinter import *
from datetime import datetime
import os
import glob

from tkinter import ttk

# Window setup
window = Tk()
window.geometry("1008x630+336+210")
mainframe = Frame(window)
window.title("Journal")

# Tab manager
tabLogic = ttk.Notebook(window)
tab1 = ttk.Frame(tabLogic)
tab2 = ttk.Frame(tabLogic)
tab3 = ttk.Frame(tabLogic)
tabLogic.add(tab1, text = 'Write')
tabLogic.add(tab2, text = 'Read')
tabLogic.add(tab3, text = 'Display')

# Writing button logic
def submit():
    curr_time = datetime.now()
    date_time = curr_time.strftime("%Y-%m-%d")
    input = textEntry.get("1.0", 'end-1c')
    if input[-1] != '.':
        input += '.'
    if not len(input) == 0:
        with open(date_time + '.txt', 'a') as file:
            file.write(input + "\n&\n")
    textEntry.delete(1.0, END)
    textEntry.insert(END, "Submitted")


"""
# Writing tab
textEntry = Text(tab1, height = 30, width = 108)
textEntry.pack()
textEntry.insert(END, "")
textEntry.grid(column = 0, row = 0, ipady = 10)

# Writing button framework
diaryWriteButton = Button(tab1, text = "Submit", command = submit)
diaryWriteButton.grid(column = 0, row = 1, pady = 10)
"""

# Reading tab
# TODO: implement 'save changes' logic
textEntry = Text(tab1, height = 30, width = 108)
textEntry.pack()
textEntry.insert(END, "")
textEntry.grid(column = 1, row = 3, pady = 10)

# Selecting option from dropdown menu

Label(tab1, text = "Write an entry").grid(row = 1, column = 1, padx = 416, pady = 5)
diaryWriteButton = Button(tab1, text = "Submit", command = submit)
diaryWriteButton.grid(column = 1, row = 2, pady = 5)




# --------------------------------------------------------
# Creating a sorted list of text files from the directory
dir = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(dir, '*.txt')
clean_filename = os.path.basename(filename)
entry_list = glob.glob(clean_filename)
entry_list.remove('initial.txt')
entry_list.sort(reverse = True)

# Dropdown menu logic
dropdownSetting = StringVar(window)
dropdownSetting.set('Journal Entries') # TODO: make sure that 'Journal Entries' isn't an accepted string
readFileSelection = 'initial.txt'
def readFile(): # TODO: implement readFile
    if dropdownSetting.get() != 'Journal Entries':
        readFileSelection = dropdownSetting.get()
        filename = readFileSelection
        textReading.delete(1.0,END)
        textReading.insert('end', open(filename, 'r').read())

# Reading tab
textReading = Text(tab2, height = 30, width = 108)
textReading.grid(column = 1, row = 6, pady = 10)
filename = readFileSelection
textReading.insert('end', open(filename,'r').read())

# Selecting option from dropdown menu
popupMenu = OptionMenu(tab2, dropdownSetting, *entry_list)
Label(tab2, text = "Choose an entry").grid(row = 1, column = 1, padx = 416, pady = 5)
diaryReadButton = Button(tab2, text = 'Open', command = readFile)
diaryReadButton.grid(row = 3, column = 1)
popupMenu.grid(row = 2, column = 1)
# ------------------------------------------------------------------

# Data display tab
label = Label(tab3, text = "dataDisplay")
label.grid(column = 0, row = 0)


# ---------------------------------------------------------------------------------#
# Sentiment analysis                                                               #
# ---------------------------------------------------------------------------------#
def print_result(annotations):
    score = annotations.document_sentiment.score
    magnitude = annotations.document_sentiment.magnitude

    for index, sentence in enumerate(annotations.sentences):
        sentence_sentiment = sentence.sentiment.score
        print('Sentence {} has a sentiment score of {}'.format(
            index, sentence_sentiment))

    print('Overall Sentiment: score of {} with magnitude of {}'.format(
        score, magnitude))
    return 0


def analyze(file):
    """Run a sentiment analysis request on text within a passed filename."""
    client = language.LanguageServiceClient()

    with open(file, 'r') as review_file:
        # Instantiates a plain text document.
        content = review_file.read()

    document = types.Document(
        content=content,
        type=enums.Document.Type.PLAIN_TEXT)
    annotations = client.analyze_sentiment(document=document)

    # Print the results
    print_result(annotations)

dir = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(dir, '*.txt')
clean_filename = os.path.basename(filename)
entry_list = glob.glob(clean_filename)
entry_list.remove('initial.txt')
entry_list.sort(reverse = True)

def Sentiment_Analysis
    for file in entry_list:
        analyze(file)
# ---------------------------------------------------------------------------------#
# ---------------------------------------------------------------------------------#




# Ending logic
tabLogic.pack(expand = 1, fill = 'both')

window.mainloop()