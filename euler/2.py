

ram=0
f =1
i = 1 
n=0
while i<=4000000:
    ram = i
    i+=f
    f=ram
    if i % 2 == 0:
        n+=i
print(n)
    