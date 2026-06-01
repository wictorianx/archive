import random
chosen = []
deck = []
win = 21
def setup():
    global chosen
    global deck
    chosen = []
    deck = [1,2,3,4,5,6,7,8,9,10,10,10,10]*4
def RandomCard():
    global chosen
    global deck
    randomCard = deck[random.randint(0,len(deck)-1)]
    chosen.append(randomCard)
    #print(f"removing {randomCard}")
    #print(f"from {deck}")
    deck.remove(randomCard)
    return(randomCard)
def Total(cards):
    global win
    sum = 0
    for i in (cards):
        sum += i
    for i in (cards):
        if i == 1:
            if sum + 10 <= win:
                sum += 10
    return sum
def Bank():
    global win
    cards = [RandomCard(),RandomCard()]
    while Total(cards) < 17:
        cards.append(RandomCard())
    if Total(cards) == win:
        if len(cards) == 2:
            return 1
        else:
            return win
    else:
        return Total(cards)
def bot(tolerance):
    global win
    cards = [RandomCard(),RandomCard()]
    while Total(cards) < tolerance:
        cards.append(RandomCard())
    if Total(cards) == win:
        if len(cards) == 2:
            return 1
        else:
            return win
    else:
        return Total(cards)
results = [0,0,0,0,0,0,0,0,0,0,0,0,0,0] # bank,12,13,14,15,16,17,18,19,20,21,smart risky, samrt safe, 0
small = 0
small = 1 
def smartBot(risk):
    global small
    global big
    global deck
    cards = [RandomCard(),RandomCard()]
    big = 0
    small = 0
    def algo(cards):
        global small
        global big
        threshold = 21-Total(cards)
        for i in deck:
            if i > threshold:
                big +=1
            else:
                small +=1
        if risk:
            if small >= big:
                cards.append(RandomCard())
        else:
            if small > big:
                cards.append(RandomCard())
        return(cards)
    while(True):
        cards = algo(cards)
        init = Total(cards)
        while(True):
            cards=algo(cards)
            if cards == init:
                break
        break
    global win
    if Total(cards) == win and len((cards)) == (win-1)/10:
        return(1)
    else:
        return(Total(cards))
for i in range(100):
    setup()
    bank = Bank()
    bot12 = bot(12)
    bot13 = bot(13)
    bot14 = bot(14)
    bot15 = bot(15)
    bot16 = bot(16)
    bot17 = bot(17)
    bot18 = bot(18)
    bot19 = bot(19)
    bot20 = bot(20)
    bot21 = bot(21)
    #risky = smartBot(True)
    #safe = smartBot(False)
    bots = [bot12, bot13, bot14, bot15, bot16,bot17,bot18,bot19,bot20,bot21]#,risky,safe]
    if bank == 1:
        for i in range(len(bots)):
            if bots[i] == 1:
                pass
            else:
                results[i+1] -= 1
    else:
        for i in range(len(bots)):
            if bots[i] == bank:
                pass
            elif bots[i] > bank:
                results[i+1] += 1
            elif bots[i] < bank:
                results[i+1] -= 1
print(results)
            
