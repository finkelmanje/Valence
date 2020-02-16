import tkinter
from tkinter import *
from tkinter import ttk
from datetime import datetime
import os
import glob
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
from grid import Grid

# Window setup
window = Tk()
window.geometry("1008x630+336+210")
mainframe = Frame(window)
window.title("Valence Journal")

# Tab manager
tabLogic = ttk.Notebook(window)
tab1 = ttk.Frame(tabLogic)
tab2 = ttk.Frame(tabLogic)
tab3 = ttk.Frame(tabLogic)
tabLogic.add(tab1, text = 'Write')
tabLogic.add(tab2, text = 'Read')
tabLogic.add(tab3, text = 'Display')

emptylist = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]

# Writing button logic
def submit(): # TODO: create empty 'initial.json' text file
    curr_time = datetime.now()
    date_time = curr_time.strftime("%Y-%m-%d")
    input = textEntry.get("1.0", 'end-1c')
    if input[-1] != '.':
        input += '.'
    if not len(input) == 0:
        with open(date_time + '.json', 'a') as file:
            file.write(input + "\n")
    textEntry.delete(1.0, END)
    textEntry.insert(END, "Submitted")

# Writing tab
textEntry = Text(tab1, height = 30, width = 108)
textEntry.pack()
textEntry.insert(END, "")
textEntry.grid(column = 1, row = 3, pady = 10)
Label(tab1, text = "Write an entry").grid(row = 1, column = 1, padx = 416, pady = 5)
diaryWriteButton = Button(tab1, text = "Submit", command = submit)
diaryWriteButton.grid(column = 1, row = 2, pady = 5)

# --------------------------------------------------------
# Creating a sorted list of text files from the directory
dir = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(dir, '*.json')
clean_filename = os.path.basename(filename)
entryList = glob.glob(clean_filename)
entryList.remove('initial.json')
entryList.sort(reverse = True)

# Dropdown menu logic
dropdownSetting = StringVar(tab2)
dropdownSetting.set('Journal Entries')
readFileSelection = 'initial.json'
def readFile():
    if dropdownSetting.get() != 'Journal Entries':
        readFileSelection = dropdownSetting.get()
        filename = readFileSelection
        textReading.delete(1.0,END)
        textReading.insert('end', open(filename, 'r').read())

# Reading tab
# TODO: implement 'save changes' logic
textReading = Text(tab2, height = 30, width = 108)
textReading.grid(column = 1, row = 6, pady = 10)
filename = readFileSelection
textReading.insert('end', open(filename,'r').read())

# Selecting option from dropdown menu
popupMenu = OptionMenu(tab2, dropdownSetting, *entryList)
Label(tab2, text = "Choose an entry").grid(row = 1, column = 1, padx = 416, pady = 5)
diaryReadButton = Button(tab2, text = 'Open', command = readFile)
diaryReadButton.grid(row = 3, column = 1)
popupMenu.grid(row = 2, column = 1)
# ------------------------------------------------------------------


# ---------------------------------------------------------------------------------#
# Sentiment analysis                                                               #
# ---------------------------------------------------------------------------------#
def returnScore(file):
    client = language.LanguageServiceClient()

    with open(file, 'r') as review_file:
        # Instantiates a plain text document.
        content = review_file.read()

    document = types.Document(
        content=content,
        type=enums.Document.Type.PLAIN_TEXT)
    annotations = client.analyze_sentiment(document=document)
    score = annotations.document_sentiment.score
    return score

def returnMagnitude(file):
    client = language.LanguageServiceClient()

    with open(file, 'r') as review_file:
        # Instantiates a plain text document.
        content = review_file.read()

    document = types.Document(
        content=content,
        type=enums.Document.Type.PLAIN_TEXT)
    annotations = client.analyze_sentiment(document=document)
    magnitude = annotations.document_sentiment.magnitude
    return magnitude

def sentimentAnalysis():
    for file in entryList:
        returnScore(file)
# ---------------------------------------------------------------------------------#
# ---------------------------------------------------------------------------------#

def analyzeYearList(year):
    examinedYear = []
    yearToScan = generateYear(year)
    for day in yearToScan:
        if day == 2 or day == []:
            examinedYear.append(2)
        else:
            examinedYear.append(returnScore(day))
    return examinedYear

# ---------------------------------------------------------------------------------#
# Data visualization                                                               #
# ---------------------------------------------------------------------------------#
SHIFT = 6
def draw_grid_canvas(grid, canvas, scale):
    canvas.delete('all')
    # color logic
    for y in range(31):
        for x in range(12):
            if grid.get(x, y) <= 1 and grid.get(x, y) >= 0.7144:
                color = 'red'
            elif grid.get(x, y) <= 0.7143 and grid.get(x, y) >= 0.4287:
                color = 'orange'
            elif grid.get(x, y) <= 0.4286 and grid.get(x, y) >= 0.143:
                color = 'yellow'
            elif grid.get(x, y) <= 0.1429 and grid.get(x, y) >= -0.1427:
                color = 'green'
            elif grid.get(x, y) <= -0.1428 and grid.get(x, y) >= -0.4284:
                color = 'blue'
            elif grid.get(x, y) <= -0.4285 and grid.get(x, y) >= -0.7141:
                color = 'indigo'
            elif grid.get(x, y) <= -0.7142 and grid.get(x, y) >= -1:
                color = 'violet'
            elif grid.get(x, y) == 2:
                color = 'white'
            rx = 1 + x * scale
            ry = 1 + y * scale
            canvas.create_rectangle(rx, ry, rx + scale, ry + scale, fill=color, outline='black')


def make_gui(top, width, height):
    top.title('Data visualizer')
    canvas = tkinter.Canvas(top, width=width, height=height, name='canvas')
    canvas.xview_scroll(SHIFT, "units")
    canvas.yview_scroll(SHIFT, "units")
    canvas.grid(row=1, columnspan=12, sticky='w', padx=20, ipady=5)
    top.update()
    return canvas


# TODO: LEAP YEARS
# TODO: code to generate initial.json and tvl.json
# TODO: remember what tvl stands for lmao

def main(tvl):
    width = 12
    height = 31
    global SIDE
    SIDE = 30
    top = tkinter.Tk()
    canvas = make_gui(top, width * SIDE + 2, height * SIDE + 2)
    # tvl = ['b', 'd', 'c', 'b', 'a', 'c', 'a', 'c', 'c', 'b', 'b', 'a', 'c', 'a', 'd', 'a', 'a', 'b', 'b', 'd', 'd', 'd', 'a', 'a', 'd', 'b', 'a', 'c', 'd', 'a', 'a', 'd', 'd', 'b', 'd', 'c', 'c', 'a', 'b', 'a', 'c', 'c', 'a', 'c', 'a', 'a', 'b', 'a', 'c', 'c', 'd', 'b', 'a', 'c', 'a', 'd', 'd', 'a', 'd', 'b', 'a', 'b', 'b', 'd', 'c', 'a', 'd', 'b', 'd', 'b', 'd', 'c', 'c', 'b', 'c', 'c', 'd', 'a', 'd', 'd', 'd', 'c', 'd', 'd', 'a', 'b', 'b', 'a', 'c', 'c', 'b', 'd', 'b', 'c', 'b', 'c', 'a', 'd', 'b', 'c', 'd', 'c', 'a', 'd', 'd', 'a', 'a', 'b', 'd', 'c', 'b', 'c', 'b', 'c', 'a', 'c', 'c', 'c', 'c', 'b', 'c', 'd', 'a', 'c', 'b', 'a', 'd', 'b', 'b', 'b', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'd', 'a', 'b', 'a', 'b', 'c', 'c', 'a', 'a', 'c', 'd', 'b', 'd', 'd', 'd', 'c', 'a', 'a', 'c', 'c', 'b', 'b', 'd', 'c', 'c', 'd', 'c', 'd', 'a', 'a', 'd', 'a', 'a', 'd', 'c', 'b', 'c', 'a', 'b', 'c', 'c', 'a', 'd', 'a', 'a', 'a', 'd', 'b', 'c', 'b', 'c', 'b', 'a', 'b', 'a', 'a', 'b', 'a', 'd', 'c', 'c', 'b', 'a', 'c', 'a', 'd', 'c', 'b', 'b', 'c', 'd', 'c', 'd', 'a', 'c', 'b', 'a', 'b', 'b', 'b', 'c', 'b', 'b', 'd', 'd', 'd', 'c', 'd', 'c', 'c', 'b', 'a', 'c', 'c', 'b', 'b', 'a', 'b', 'd', 'd', 'c', 'b', 'c', 'c', 'a', 'b', 'b', 'c', 'c', 'b', 'b', 'a', 'd', 'a', 'a', 'd', 'd', 'b', 'd', 'b', 'd', 'd', 'd', 'a', 'c', 'a', 'd', 'd', 'b', 'a', 'a', 'd', 'c', 'd', 'a', 'd', 'b', 'a', 'd', 'c', 'a', 'a', 'c', 'b', 'a', 'c', 'c', 'd', 'b', 'd', 'd', 'd', 'd', 'a', 'b', 'c', 'd', 'b', 'a', 'a', 'c', 'c', 'd', 'b', 'a', 'a', 'b', 'c', 'a', 'c', 'a', 'd', 'd', 'd', 'c', 'b', 'b', 'd', 'c', 'a', 'b', 'b', 'b', 'a', 'b', 'a', 'c', 'a', 'a', 'a', 'b', 'd', 'd', 'b', 'c', 'd', 'a', 'd', 'b', 'c', 'a', 'b', 'd', 'b', 'b', 'b', 'a', 'a', 'c', 'd', 'a', 'b', 'd', 'c', 'a', 'a', 'a', 'a', 'b', 'c', 'c', 'a', 'd', 'b', 'd', 'a', 'a', 'd', 'b', 'c', 'a', 'a', 'b', 'd', 'a', 'b']
    # tvl = [0.08734, 0.38131, -0.42622, 0.46849, 0.26056, -0.82283, 0.98408, -0.11093, -0.31607, -0.86551, -0.49823, -0.11524, -0.29370, 0.87165, -0.28865, -0.87120, 0.98890, -0.54031, 0.78524, -0.44514, -0.30240, 0.37368, -0.04673, -0.91169, 0.31832, 0.20535, -0.09512, 0.58772, -0.21630, 0.94340, -0.60348, 0.10218, 0.41042, 0.03240, 0.51157, 0.96881, -0.09069, -0.63048, -0.28570, 0.39834, -0.81041, 0.55009, -0.67440, -0.88717, -0.31462, -0.02507, -0.42039, 0.35800, 0.94182, -0.03683, -0.17155, -0.92595, 0.95252, 0.79642, -0.84991, 0.16024, 0.98998, 0.95865, -0.92585, 0.28575, -0.09002, 0.06001, -0.31664, 0.80007, -0.84464, -0.14921, 0.96868, 0.17136, -0.86716, -0.61103, 0.51725, 0.72108, 0.38375, 0.66816, 0.58868, -0.85655, 0.53419, -0.64444, 0.77592, -0.47105, -0.09891, -0.26983, 0.75327, -0.24761, 0.61620, -0.32825, -0.26635, 0.96529, 0.44650, 0.54331, 0.42686, -0.08836, -0.89808, -0.23227, -0.81358, 0.35808, 0.91503, 0.63358, -0.33914, -0.11099, 0.18451, -0.40004, 0.48614, -0.04818, -0.35493, -0.31300, 0.37225, -0.10501, 0.54436, 0.23727, 0.12431, -0.32352, 0.24777, -0.26289, -0.61242, -0.92175, -0.23574, -0.50583, -0.32357, 0.42974, -0.44653, -0.09076, -0.28055, -0.26003, 0.80996, -0.16664, -0.23910, -0.40971, -0.64595, 0.36497, 0.95950, -0.88590, -0.94893, -0.30373, 0.12776, -0.79873, -0.20848, -0.38818, -0.31835, -0.72785, 0.08863, -0.24677, 0.13333, 0.73827, 0.59200, 0.65075, 0.26941, -0.09646, -0.82077, 0.36857, -0.37555, 0.47652, -0.58856, -0.06542, 0.12466, -0.64643, 0.88956, -0.31274, 0.65372, 0.90245, -0.51210, 0.04401, 0.33469, -0.87112, 0.15567, -0.63332, -0.34992, -0.25844, -0.57906, -0.41909, 0.73229, -0.83582, -0.30854, -0.15540, -0.24972, -0.24954, -0.68986, -0.63427, -0.99691, -0.04925, 0.83782, 0.11004, 0.33194, -0.11515, -0.62289, 0.92416, -0.15162, -0.62594, 0.91057, 0.62655, -0.14651, -0.60346, -0.04473, 0.29781, -0.42995, -0.12493, 0.49963, -0.29997, 0.58083, -0.39947, 0.55647, -0.07637, 0.68402, 0.12849, -0.04000, -0.48313, -0.87754, 0.11264, -0.05151, -0.54785, -0.41288, 0.74012, -0.68949, 0.85363, 0.68968, 0.27606, 0.91781, 0.89220, 0.23808, 0.75218, -0.96269, 0.97661, -0.69932, -0.14313, 0.60237, -0.71678, 0.16301, -0.25900, 0.81327, -0.27636, 0.45638, -0.04449, -0.58440, 0.65398, 0.94756, 0.75382, 0.46165, 0.13791, 0.01821, -0.70285, 0.24394, -0.24947, 0.36995, -0.19565, 0.15790, 0.92400, 0.22755, 0.42646, -0.05120, -0.53940, 0.66861, 0.35980, -0.51335, 0.55464, -0.82433, 0.88172, -0.91379, 0.96915, 0.39245, -0.41222, -0.30241, -0.33048, -0.40606, -0.86405, -0.77109, 0.56894, -0.66450, -0.36091, -0.67631, -0.59402, -0.85813, 0.16899, 0.27538, -0.29913, -0.58284, -0.68011, 0.87287, 0.18515, -0.29053, 0.54994, -0.24066, 0.66371, -0.63816, -0.27199, 0.78591, 0.89567, 0.41354, -0.09667, -0.48214, 0.35464, -0.00113, 0.96920, 0.61062, 0.14959, -0.12916, -0.13027, 0.09124, 0.01987, 0.11311, 0.89090, -0.53472, -0.00504, -0.60104, -0.23560, 0.55733, 0.16410, -0.73226, -0.31084, 0.61366, 0.96302, -0.68482, -0.90584, 0.56101, -0.47865, 0.53382, 0.59539, 0.17758, 0.47744, 0.44768, -0.36930, 0.15608, 0.09403, 0.61441, 0.61265, -0.28508, -0.03265, -0.56320, -0.70527, -0.30594, -0.92673, -0.71246, 0.20588, -0.61715, 0.62697, -0.95598, 0.98319, -0.88953, -0.42315, -0.96948, -0.05481, -0.50740, 0.70637, -0.95695, 0.15822, 0.89625, 0.83747, 0.31119, -0.19414, 0.18584, 0.38369, -0.86896, -0.80417, -0.60036, -0.10194, 0.41996, 0.79200, 0.51522, -0.25867, 0.02563, 0.30959, -0.22424, -0.37497, 0.78684, -0.72868, 0.96021, -0.70804, -0.84564, 0.39666, -0.44590, -0.18621, 0.29180, -0.50562]
    grid = Grid.build([[tvl[0], tvl[1], tvl[2], tvl[3], tvl[4], tvl[5], tvl[6], tvl[7], tvl[8], tvl[9], tvl[10], tvl[11]], [tvl[12], tvl[13], tvl[14], tvl[15], tvl[16], tvl[17], tvl[18], tvl[19], tvl[20], tvl[21], tvl[22], tvl[23]], [tvl[24], tvl[25], tvl[26], tvl[27], tvl[28], tvl[29], tvl[30], tvl[31], tvl[32], tvl[33], tvl[34], tvl[35]], [tvl[36], tvl[37], tvl[38], tvl[39], tvl[40], tvl[41], tvl[42], tvl[43], tvl[44], tvl[45], tvl[46], tvl[47]], [tvl[48], tvl[49], tvl[50], tvl[51], tvl[52], tvl[53], tvl[54], tvl[55], tvl[56], tvl[57], tvl[58], tvl[59]], [tvl[60], tvl[61], tvl[62], tvl[63], tvl[64], tvl[65], tvl[66], tvl[67], tvl[68], tvl[69], tvl[70], tvl[71]], [tvl[72], tvl[73], tvl[74], tvl[75], tvl[76], tvl[77], tvl[78], tvl[79], tvl[80], tvl[81], tvl[82], tvl[83]], [tvl[84], tvl[85], tvl[86], tvl[87], tvl[88], tvl[89], tvl[90], tvl[91], tvl[92], tvl[93], tvl[94], tvl[95]], [tvl[96], tvl[97], tvl[98], tvl[99], tvl[100], tvl[101], tvl[102], tvl[103], tvl[104], tvl[105], tvl[106], tvl[107]], [tvl[108], tvl[109], tvl[110], tvl[111], tvl[112], tvl[113], tvl[114], tvl[115], tvl[116], tvl[117], tvl[118], tvl[119]], [tvl[120], tvl[121], tvl[122], tvl[123], tvl[124], tvl[125], tvl[126], tvl[127], tvl[128], tvl[129], tvl[130], tvl[131]], [tvl[132], tvl[133], tvl[134], tvl[135], tvl[136], tvl[137], tvl[138], tvl[139], tvl[140], tvl[141], tvl[142], tvl[143]], [tvl[144], tvl[145], tvl[146], tvl[147], tvl[148], tvl[149], tvl[150], tvl[151], tvl[152], tvl[153], tvl[154], tvl[155]], [tvl[156], tvl[157], tvl[158], tvl[159], tvl[160], tvl[161], tvl[162], tvl[163], tvl[164], tvl[165], tvl[166], tvl[167]], [tvl[168], tvl[169], tvl[170], tvl[171], tvl[172], tvl[173], tvl[174], tvl[175], tvl[176], tvl[177], tvl[178], tvl[179]], [tvl[180], tvl[181], tvl[182], tvl[183], tvl[184], tvl[185], tvl[186], tvl[187], tvl[188], tvl[189], tvl[190], tvl[191]], [tvl[192], tvl[193], tvl[194], tvl[195], tvl[196], tvl[197], tvl[198], tvl[199], tvl[200], tvl[201], tvl[202], tvl[203]], [tvl[204], tvl[205], tvl[206], tvl[207], tvl[208], tvl[209], tvl[210], tvl[211], tvl[212], tvl[213], tvl[214], tvl[215]], [tvl[216], tvl[217], tvl[218], tvl[219], tvl[220], tvl[221], tvl[222], tvl[223], tvl[224], tvl[225], tvl[226], tvl[227]], [tvl[228], tvl[229], tvl[230], tvl[231], tvl[232], tvl[233], tvl[234], tvl[235], tvl[236], tvl[237], tvl[238], tvl[239]], [tvl[240], tvl[241], tvl[242], tvl[243], tvl[244], tvl[245], tvl[246], tvl[247], tvl[248], tvl[249], tvl[250], tvl[251]], [tvl[252], tvl[253], tvl[254], tvl[255], tvl[256], tvl[257], tvl[258], tvl[259], tvl[260], tvl[261], tvl[262], tvl[263]], [tvl[264], tvl[265], tvl[266], tvl[267], tvl[268], tvl[269], tvl[270], tvl[271], tvl[272], tvl[273], tvl[274], tvl[275]], [tvl[276], tvl[277], tvl[278], tvl[279], tvl[280], tvl[281], tvl[282], tvl[283], tvl[284], tvl[285], tvl[286], tvl[287]], [tvl[288], tvl[289], tvl[290], tvl[291], tvl[292], tvl[293], tvl[294], tvl[295], tvl[296], tvl[297], tvl[298], tvl[299]], [tvl[300], tvl[301], tvl[302], tvl[303], tvl[304], tvl[305], tvl[306], tvl[307], tvl[308], tvl[309], tvl[310], tvl[311]], [tvl[312], tvl[313], tvl[314], tvl[315], tvl[316], tvl[317], tvl[318], tvl[319], tvl[320], tvl[321], tvl[322], tvl[323]], [tvl[324], tvl[325], tvl[326], tvl[327], tvl[328], tvl[329], tvl[330], tvl[331], tvl[332], tvl[333], tvl[334], tvl[335]], [tvl[336], 2, tvl[338], tvl[339], tvl[340], tvl[341], tvl[342], tvl[343], tvl[344], tvl[345], tvl[346], tvl[347]], [tvl[348], 2, tvl[350], tvl[351], tvl[352], tvl[353], tvl[354], tvl[355], tvl[356], tvl[357], tvl[358], tvl[359]], [tvl[360], 2, tvl[362], 2, tvl[364], 2, tvl[366], tvl[367], 2, tvl[369], 2, tvl[371]]])

    #tvl = [0.08734, 0.38131, -0.42622, 0.46849, 0.26056, -0.82283, 0.98408, -0.11093, -0.31607, -0.86551, -0.49823, -0.11524, -0.29370, 0.87165, -0.28865, -0.87120, 0.98890, -0.54031, 0.78524, -0.44514, -0.30240, 0.37368, -0.04673, -0.91169]
    # grid = Grid.build([[tvl[0], tvl[1], tvl[2], tvl[3], tvl[4], tvl[5], tvl[6], tvl[7], 2, tvl[9], tvl[10], tvl[11]], [tvl[12], tvl[13], tvl[14], tvl[15], tvl[16], tvl[17], tvl[18], tvl[19], tvl[20], tvl[21], tvl[22], tvl[23]]])
    draw_grid_canvas(grid, canvas, SIDE)
    tkinter.mainloop()


def stringConvert(string):
    string = string[1:]
    string = string[:-1]
    li = list(string.split(", "))
    return li

def regenerateData():
    year = dataLoadSettings.get()
    tvl = analyzeYearList(year)
    with open('tvls/' + str(year) + 'tvl.json', 'w+') as tvlfile:
        tvlfile.write(str(tvl))
    main(tvl)

def loadData():
    year = dataLoadSettings.get()
    if os.path.exists('tvls/' + str(year) + 'tvl.json'):
        with open('tvls/' + str(year) + 'tvl.json', 'r') as tvlfile:
            content = tvlfile.read()
            stringList = stringConvert(content)
            tvl = [float(i) for i in stringList]
        main(tvl)
    else:
        with open('tvls/' + str(year) + 'tvl.json', 'w+') as tvlfile:
            tvlfile.write(str(emptylist))
        main(emptylist)
# ---------------------------------------------------------------------------------#
# ---------------------------------------------------------------------------------#




def yearList(year): # TODO: put function calls in order
    return [i for i in entryList if year in i]


def count_nDays(monthnumber, days, year):
    lst = []
    currentYear = yearList(str(year))
    for day in range(days):
        day = str(day + 1)
        day = day.zfill(2)
        filename = str(year) + '-' + str(monthnumber).zfill(2) + '-' + day + '.json'
        if filename in currentYear:
            lst.append(filename)
        else:
            lst.append([])
    return lst


def generateYear(year):
    m0 = [2]
    m1 = count_nDays(1, 31, year)
    m2 = count_nDays(2, 28, year)
    m3 = count_nDays(3, 31, year)
    m4 = count_nDays(4, 30, year)
    m5 = count_nDays(5, 31, year)
    m6 = count_nDays(6, 30, year)
    m7 = count_nDays(7, 31, year)
    m8 = count_nDays(8, 31, year)
    m9 = count_nDays(9, 30, year)
    m10 = count_nDays(10, 31, year)
    m11 = count_nDays(11, 30, year)
    m12 = count_nDays(12, 31, year)
    return m1 + m2 + m0 + m0 + m0 + m3 + m4 + m0 + m5 + m6 + m0 + m7 + m8 + m9 + m0 + m10 + m11 + m0 + m12

# Data display tab
Label(tab3, text = "Display Data").grid(row = 1, column = 1, padx = 416, pady = 5)
dataDisplayButton = Button(tab3, text = "load data", command = loadData)
dataDisplayButton.grid(column = 1, row = 3, pady = 5)
dataGenerateButton = Button(tab3, text = "regenerate data", command = regenerateData)
dataGenerateButton.grid(column = 1, row = 4, pady = 5)

years = [2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011, 2010, 2009, 2008, 2007, 2006, 2005, 2004, 2003, 2002, 2001, 2000]
dataLoadSettings = StringVar(tab3)
dataLoadSettings.set('2020')

popupMenu = OptionMenu(tab3, dataLoadSettings, *years)
popupMenu.grid(row = 2, column = 1)


# Ending logic
tabLogic.pack(expand = 1, fill = 'both')
window.mainloop()