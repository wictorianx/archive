'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
print ('Hello World')
import random
chances = int(input("Input Dice Faces : "))
numbers = int(input("Input Dice  Count : "))

"""
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
nums = [a,b,c,d,e,f] # change this to x many numbers according to number count
cu""" 
nums = []
for num in range(numbers):
    nums.append(0)
count=0
checklist = 0
prelist = 0
while(True):
    for i in range (numbers):
        nums[i] = random.randint(0,chances)
        count +=1
    checklist = nums[0]
    for t in range (numbers):
        try:
            if (nums[t]==nums[t+1]):
                prelist = True
            else:
                prelist = False
                break
        except:
            pass
    if prelist:
        break
print(count)
