
ans=0
ans0 = 0 
p = 0
def palindromic (x, a):
    ans = ans0
    p = x * a 
    if ((str (p)) == (str (p)[::-1]) and p > ans):
        ans = p 
        return (ans)
'''d1 = 100
d2 = 100
while(d1<1000):
    while(palindromic(d1*d2) != true):
        d2++
    d1++
print(d1*d2)'''
x = 100
a= 100
while(ans < 10000):
    print (palindromic (x, a)) 
    while( x < 1000):
        x += 1 
        print (palindromic (x, a)) 
        while(a < 1000):
            a += 1 
            print (palindromic (x, a))






