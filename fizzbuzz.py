def p (x):
    print(x)

def fizzbuzz(x):
    for i in range(x+1):
        o = ""
        if i % 3 == 0:
            o += "fizz"
        if i% 5 == 0:
            o+= "buzz"
        if o == "":
            o+=i
        p(o)
        
fizzbuzz(100)
