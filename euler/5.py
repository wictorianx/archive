'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''

smallest = []
print ('Hello World')
x=1
a=1
y=0
z = 0
while(z!=20):
    z+=1
    a+=1
    while(y != 20):
        x+=1
        y+=1
        if ( x%a == 0):
            x/=a
            smallest.append(x)
    
    

    