
ans = 0
def sumOf(l):
    x = 0
    for i in l:
        x += i
    return (x)
def d(x):
    y = []
    for i in range(x-1):
        if x % (i+1) == 0:
            y.append(i+1)
    return(sumOf(y))

index=0
while(index<10000):
    index+=1
    a = d(index)
    b = d(a)
    if index == b and a != b :
        ans += a
print(ans)





