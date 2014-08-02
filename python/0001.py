#!/usr/bin/env python

#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The totalSum of these multiples is 23.
#Find the totalSum of all the multiples of 3 or 5 below 1000.

def isMultiple(curNum):
    if (curNum % 3 == 0) or (curNum % 5 == 0):
        return True 
    else:
        return False
   
def main():
    totalSum = 0
    for number in range(1000):
        if isMultiple(number):
            totalSum = totalSum + number

    print totalSum

main()
