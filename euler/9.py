

for num in range(1, 1000):
    for dig in range(num, 1000 - num):
        i = 1000 - num - dig
        if num * num + dig * dig == i * i:
            print(num, dig, i)
            print("Product: {}".format(num * dig * i))
