sumall = 0
i =1
three = 0
five = 0
while(True):
    if three<1000:
        three = i*3
        i= i+1
        if three == 1002:
            break
        sumall=sumall+three
i = 1
while(True):
    if five<1000 and five%3!=0:
        sumall = sumall + five
        five = i*5
        i = i+1
        if five == 1000:
            break
print(sumall-three)
        
    
        

















