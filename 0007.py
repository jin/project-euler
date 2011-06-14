# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10001st prime number?

import math
import time

start = time.time()

def isPrime(val):
    i = 3
    while (i<(val/2)):
        if (val % i == 0):
            return False
        else:
            i += 2
    return True

numPrime = 0
curNum = 1 

while (numPrime < 10001):
    if (isPrime(curNum)):
        numPrime+=1
    curNum+=2
    
print curNum-2
end = time.time()
print (end - start)