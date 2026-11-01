import os
"""
dirs = [os.getcwd(),os.listdir()]
max_iter = 100
iter = 0
while dirs[len(dirs)-1] != dirs[len(dirs)-2]:
    iter += 1
    o = []
    for i in dirs[len(dirs)-1]:
        try:
            os.chdir(i)
            o.append(os.listdir())
            print(o)
        except:
            pass
    dirs.append(o)
    if iter == max_iter:
        print(43)
        print(8)
        print(dirs[len(dirs)-1])
        print(99999999)
        print(dirs[len(dirs)-2])
        print(len(dirs))
        break

"""
"""print(dirs[len(dirs)-1])
print(dirs)"""

a = os.listdir()
b = []
def f(a):
    global b
    for i in a:
        try:
            os.chdir(i)
            b.append(os.listdir())
            b.remove(i)
        except:
            print(f"{i} in {os.getcwd()}")
def m(a):
    global b
    while True:
        temp = b
        f(a)
        if b == temp:
            break

m(a)
print(b)
y = input()






