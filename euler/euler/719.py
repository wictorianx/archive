
print ('Hello World')
a = 10*10*10*10
tar = pow(10, 12)
ums = 41333
def check(x):
    s=0
    for i in str(x*x):
        s+=int(i)
    if s == x:
        return(True)
while(True):
    a+=1
    if check(a):
        ums+=a
    if a == tar:
        break
print(ums)
