from tkinter import *
import os
import PyPDF2
import pyttsx3
import time
import easygui 
import tkinter.ttk as ttk
global word 
global currentword
global delay
currentword = 0
global new 
new = True
global id
global filename
global db
db = open("spreederDatabse.txt", "a+")
global past
def load():
    global db
    global filename
    global currentword
    global new
    global i 
    db = open("database","w+")
    past = db.readlines()
    index = -1
    for i in past:
        index += 1
        if i[0] == filename:
            currentword = i[2]
            new  = False
            i = index
def getSpeed(wpm):
    wps = wpm/60
    delay = int(1/wps*1000)
    return(delay)
def openFile():
    global filename
    myFile = easygui.fileopenbox()
    filename = myFile
    return myFile
def getTextFromPDF(location):
    output = ""
    book = open(location,"rb")
    pdfReader = PyPDF2.PdfFileReader(book)
    pageNumber = pdfReader.numPages
    for fakePageNum in range(pageNumber):
        pageNum = fakePageNum #"+1"
        page = pdfReader.getPage(pageNum)
        text = page.extractText()
        if "PageDivider" in text:
            print("text cant contain PageDivider")
            break
        output += text + "PageDivider"
    return output
def display(textList,outsource):
    global delay
    global word
    global currentword
    textList = textList.split(" ")
    for element in textList:
        time.sleep(delay)
        word = element
        currentword += 1
        outsource.configure(text=word)
        #print(word)
quited = False
def quitUp():
    global db
    global id
    global past
    global filename
    global currentword
    global i 
    global quited
    """if new:
        db.write(filename,i)
    else:
        past[id][1] = i
    db.write(past)"""
    quited = True

#load()
delay = getSpeed(120)
"""filename = "Of Mice and Men - Full Text.pdf"
textlist = getTextFromPDF(filename)
textlist = textlist.split(" ")
            
"""
textlist = []
word = 0
curPage = 0
i = 0

def refresh_label():
    global i
    global label0
    global paused
    global pageNums
    global label1
    
    label1.configure(text=i)
    if not paused:
        if i<len(textlist)-1:
            trpl = textlist[i]
            otp = ""
            if type(trpl) == list:
                for el in trpl:
                    otp+=el+" "
            else:
                otp = trpl
            label0.configure(text=otp,font=("Arial",130))
            i += 1
            my_slider.config(value=i)
            "curPage = page(pageNums)"
    if not quited: 
        label0.after(delay, refresh_label)
    else:
        quit()

paused = True
def pause():
    global paused
    if paused:
        paused = False
    else:
        paused = True

root = Tk()
root.geometry("900x600")
label0 = Label(root,text = word)
label0.pack()
B = Button(root, text ="Pause", command = pause)
B.pack()
quitButton = Button(root, text ="Quit", command = quitUp)
quitButton.pack()
master_frame = Frame(root)
master_frame.pack(pady=20)
def slide(x):
    global i
    i = int(my_slider.get())
    print(x)

def setWpm():
    pass
label1 = Label(root,text = word)
label0.after(1000, refresh_label())

label1.pack()
my_slider = ttk.Scale(master_frame, from_=0, to=100, orient=HORIZONTAL, value=0, command=slide, length=360)
my_slider.pack()
pageNums = []
def HandleText(text):
    #global pageNums
    try:
        text = text.split("PageDivisor")
    except:
        pass
    for i in range(len(text)):
        text[i] = text[i].split(" ")
    pageNums = []
    for i in text:
        pageNums.append(len(i))
    text = text[0]

        
    return text
def page(pageNums):
    global i
    b = page = 0
    for t in pageNums:
        if b-t >= 0:
            b-=t
            page +=1
        else:
            return(page)




def New():
    global textlist
    global paused

    myFile = openFile()
    if myFile[-4:] == ".pdf": #last 4 items
        text = getTextFromPDF(myFile)
    elif myFile[-4:] == ".txt": #last 4 items
        imp = open(myFile,"rb")
        text = imp.readlines()
        print(text)
    textlist = HandleText(text)
    
    my_slider.config(value=0,to = len(textlist)-1)
    paused = False
    

def Openf():
    global textlist
    global paused
    paused = False
my_menu = Menu(root)

root.config(menu=my_menu)

file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=Openf)
file_menu.add_command(label="New", command=New)

settings = Menu(my_menu)
my_menu.add_cascade(label="Settings", menu=settings)
settings.add_command(label="Set Words Per Minute", command=setWpm) 





root.mainloop()