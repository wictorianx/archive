def conv(inp):
    inX = 0
    tmp = inp
    inp = []
    for x in tmp:
        inp.append(x)
    print(inp)
    out = []
    ops = ["+","-","/","*"]
    for i in range(len(inp)):
        print(i)
        try:
            if inp[i-inX] in ops:
                out.append(inp[:i])
                for t in range(i):
                    inp.pop(t-inX)
                inX+=i
        except:
            print(f'i : ')
            print(i-inX)
            print(f'list : ')
            print(inp)
    return(out)

print(conv("34+67+89"))

