def factorian(x):
    answer = 1
    for a in range (x):
        a = a+1
        answer *= a
    return(answer)
bigSum = 0
for i in str(factorian(100)):
    bigSum+=int(i)
print(bigSum)