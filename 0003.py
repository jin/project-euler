#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

import math
factor = 0  

def isPrime(val):
    i = 2
    while (i<(val/2)):
        if (val % i == 0):
            return False
        else:
            i += 1 
    return True

while (factor < 600851475143):
    factor = factor + 1 
    if (600851475143 % factor == 0) and (isPrime(factor)):
        print factor


