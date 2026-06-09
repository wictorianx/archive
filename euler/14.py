def sequence(number):
    length = 0
    while number != 1:
        if number == 0:
            break
        elif number%2 == 0:
            number = number/2
        else:
            number = number*3+1
        length += 1
    return(length+1)
biggest = 0
answer = 0
for i in range(1000000):
    chain = sequence(i)
    if chain > biggest:
        biggest = chain
        answer = i
print(answer)

    
