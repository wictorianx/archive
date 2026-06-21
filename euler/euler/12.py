
num = 500
def tri(x):
    a = 0
    for i in range(x):
        a += i + 1
    return (a)
def div(x):
    a=0
    for i in range(x):
        if x % (i + 1) == 0:
            a += 1
    return(a)
while(True):
    num += 1 
    if div(tri(num)) >= 500:
        print(num)
        break