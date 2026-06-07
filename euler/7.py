
primes = [2,3,5,7]
i = 10
p = 0
while(len(primes)<=5):
    i+=1
    p=0
    while(i not in primes):
        if primes[p]!=0:
            if i % primes[p] ==0:
                continue
            else:
                primes.append(p)
        p+=1
        
print(primes[5])
            
        
    
