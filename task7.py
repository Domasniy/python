from math import factorial

def fact(n):
    for el in list(range(1,n+1)):
        yield factorial(el)


for el in fact(10):
    print(el)


    
