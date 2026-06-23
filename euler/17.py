
theSum = 0
secondDig = 0
thirdDig = 0
for i in range(1001):
    thirdDig == False
    firstDig = int(str(i)[::-1][0])
    if i>9:
        secondDig = int(str(i)[::-1][1])
        if i>99:
            thirdDig = int(str(i)[::-1][2])
    if firstDig == 1 or firstDig == 2 or firstDig == 6:
        theSum += 3
    elif firstDig == 3 or firstDig == 7 or firstDig == 8:
        theSum+=5
    elif firstDig == 4 or firstDig == 9:
        theSum+=4
    if secondDig == 1:
        theSum +=1
    elif secondDig == 2 or secondDig == 3 or secondDig == 4 or secondDig == 8 or secondDig == 9:
        theSum += 6
    elif secondDig == 5 or secondDig == 6:
        theSum +=5
    else:
        theSum += secondDig
    if thirdDig == 1 or thirdDig == 2 or thirdDig == 6:
        theSum += 10
    elif thirdDig == 3 or thirdDig == 7 or  thirdDig == 8:
        theSum += 12
    elif thirdDig == 4 or thirdDig == 5 or thirdDig == 9:
        theSum += 11 
print(theSum)

