#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
import sys
import time

start = time.time()

def isFactor(num):
    for factor in range(11,20):
        if (num % factor != 0): return False
    return True

def main():
    num = 2520 
    while (True):
        num += 2520
        if (isFactor(num)): 
            print num
            end = time.time()
            print (end - start)
            sys.exit()
            
main()