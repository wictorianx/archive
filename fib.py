#25
def last(xList):
    return(xList[len(xList)-1])
def xLast(xList):
    return(xList[len(xList)-2])
def fibonacci():
    index = 0
    sequence = [1,1]
    while(len(str(last(sequence)))!=1000):
        sequence.append(last(sequence)+xLast(sequence))
    return(len(sequence))
print(fibonacci())
