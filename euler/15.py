
print ('Hello World')
def factorial(x):
    result = 1
    for i in range(x):
        result *= i+1 
    return(result)
print(factorial(40)/((factorial(20)*factorial(20))))
