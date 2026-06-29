def low (word):
    a = []
    d = 0
    for i in range(len(word)):
        a.append(word[i])
    for c in a:
        a[d]=c.lower()
        d +=1
    e = ""
    for f in a:
        e+=f
    return(e)
def lowList(iList):
    a = 0
    for i in iList:
        iList[a] = i.lower()
        a+=1
ex = 0
while(True):
    if ex != 0:
        word = input("Kelime Giriniz: ")
    else:
        word = "osman"
    ex = 1
    h = 5
    a = word.split(" ")
    p = ""
    while "" in a:
        a.remove("")
    for i in range(len(a)-1):
        p+=a[i]
        p+=" "
    p += a[len(a)-1]
    solved = False
    l = []
    rList = []
    for i in range(10):
        print("\n")
    while(solved == False and h>0):
        d = ""
        for t in p:
            if t not in l and t!=" ":
                d+= "_"
            elif t == " ":
                d+=" "
            else:
                d+= t
        print(d)
        if d == p:
            print(" \n Tebrikler kazandınız \n ")
            solved = True
        if solved == False:
            w = input("\n harf veya kelime giriniz: ")
            if w == "":
                print("Lütfen bir kelime giriniz")
            if low(w) == low(p):
                print("\n Tebrikler kazandınız \n ")
                solved = True
            elif low(w) in low(p) and low(w) not in l:
                l.append(w)
                print("\n Tebrikler, harf, kelimede bulunmakta\n ")
            else:
                h -= 1
                print("\n Yanlış cevap!, kalan canlar : " + str(h)+" \n ")
        
                

