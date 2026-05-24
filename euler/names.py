names = open("p022_names.txt","r+")
names = names.sort()
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
total = 0
index = 0

def value(name):
    global letters
    val = 0
    for letter in name:
        i = letters.index(letter)+1
        val += i
    return(val)
for name in names:
    curr_total = 0
    index += 1
    curr_total+=value(name)*index
    total += curr_total
print(total)


