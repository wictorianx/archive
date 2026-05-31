import PyPDF2
from datetime import datetime
start=datetime.now()
print(0)
filename = "Of Mice and Men - Full Text.pdf"
book = open(filename,"rb")
pdfReader = PyPDF2.PdfFileReader(book)
pageNum = pdfReader.numPages
output = ""
for num in range(pageNum):
    page = pdfReader.getPage(num)
    text = page.extractText()
    output+=text
def breakText(text,punctuation = '"'):
    textList = text.split(" ")
    for elementNumber in range(len(textList)):
        if textList[elementNumber] in punctuation:
            textList[elementNumber-1]+=textList[elementNumber]
            textList.pop(elementNumber)
    return textList
output = breakText(output)
file = open(filename[:-4]+".txt","w+")
temp = output
output = ""
for i in temp:
    output += i + " "
"file.write(output)"
for t in output:
    try:
        file.write(t+" ")
    except:
        print(f"error occured can't write {t} passing item")
print(start-datetime.now())