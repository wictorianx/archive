f=open("names.txt","r")
names = f.readline().split('","')
names[0] = "MARY"
names[len(names)-1] = "ALONSO"
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","y","u","v","w","x","y","z"]
Xsum = 0
names.sort()
print(names)
for Xname in range(len(names)):
    name = names[Xname].lower()
    Lsum = 0
    for letter in name():
        value = letters.index(letter)+1
        Lsum += value
    Xsum += (Xname+1)*Lsum
print(Xsum)