#===============================================================================
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# 
# Find the sum of all the primes below two million.
#===============================================================================

import time
import math

start = time.time()
primes = [2]



def isPrime(val):
    for prime in primes[:int(math.sqrt((len(primes))))+1]:
        if (val%prime==0):
            return False
    primes.append(val)
    return True 
    

def main():
    for val in range(3,2000000,2):
        isPrime(val)
    print len(primes)
    print sum(primes)
    print time.time() - start
    
main()
