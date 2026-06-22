
largeSum = 0
f=open("num.txt", "r")
for i  in range(100):
    largeSum += int(f.readline())
print(largeSum)