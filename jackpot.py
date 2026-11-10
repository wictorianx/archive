from random import randint
players = ["ali","mehmet","ensar"]
investments = [31,36.5,52]
def main():
    global players
    global investments
    def randomize(l):
        output = []
        langidi_lan_lan = len(l)
        for i in range(langidi_lan_lan):
            r = randint(0, len(l)-1)
            output.append(l[r])
            l.remove(l[r])
        return(output)

    def topla(liste):
        output = 0
        for i in liste:
            output += i
        return(output)
    sum_of_investment = topla(investments)
    remainder = sum_of_investment % 1  
    if remainder != 0:
        coefficient = 1/remainder  
    for i in range(len(investments)):
        investments[i]*= coefficient
    base = []
    c=-1
    for i in investments:
        c+=1
        for l in range(int(i)):
            base.append(c)
    base = randomize(base)
    random_index = randint(0, len(base))
    corr_num = base[random_index]
    winner = players[corr_num]
    return(winner)

winners = []
for i in range(100):
    winner = main()
    print(winner)
    winners.append(winner)
    for t in invesments:
        print(f'{t} : {winners.count(t)}')

