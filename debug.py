a = """
08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
"""
columnLists = []
dList1 = []
dList2 = []
true = True
i = 4
state = 1
rows = a.replace("\r", "").split("\n")
for row in rows:
    if(not len(row)):
        continue
    rowLists.append(row.split())
for c in range(1):
    columnLists.append([rowLists[0][c]])
for d in range(1):
    for e in range(19):
        e += 1
        columnLists[d].append(rowLists[e][d])
for g in range(32):
    dList1.append([])
h = 0
while(true):
    for f in range(i-1):
        try:
            dList1[h].append(columnLists[f][20-i+f])
        except:
            pass
    if state == 1:
        i+=1
        if i == 20:
            state = 2
    elif state == 2:
        i -= 1
        if i == 0:
            state = 3
    elif state == 3:
        i += 1
        if i == 5:
            break
    h += 1
    print(dList1)
    
        








