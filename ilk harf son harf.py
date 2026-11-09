a = 0
prev = []
last = ""
while(True):
    
    if a == 0:
        last = input("seed girin")
    else:
        if a % 2 == 0:
            last = input("ikinci oyuncu sırası = ")
            if last not in prev:
                prev.append(last)
            else:
                print("birinci oyuncu kazandı")
                break
        else:
            last = input("birinci oyuncu sırası = ")
            if last not in prev:
                prev.append(last)
            else:
                print("birinci oyuncu kazandı")
                break


    a += 1
