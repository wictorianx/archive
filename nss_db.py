import pickle
val_list = []
filename = 'db.pkl'
outfile = open(filename,'rb+')
def init():
    global val_list
    global outfile
    try:
        while(True):
            val_list.append(pickle.load(outfile))
    except:
        print("Some error occured while importing db, possibly non-existent")
    print(val_list)
init()
while(True):
    x = input()
    if x == "q":
        break
    if x not in val_list:
        val_list.append(x)
        print(val_list)


pickle.dump(val_list,outfile)
print("Dumped")