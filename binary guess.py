import random

while(True):
    rang = input("Input range ")
    ran = random.randint(1,rang)
    while(True):
        tahmin = input("tahmin girniz")
        if tahmin == ran:
            print("True")
            break
        elif tahmin < ran:
            print("number is bigger")
        else:
            print("number is smaller")
