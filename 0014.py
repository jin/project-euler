#===============================================================================
# The following iterative sequence is defined for the set of positive integers:
# 
# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)
# 
# Using the rule above and starting with 13, we generate the following sequence:
# 
# 13  40  20  10  5  16  8  4  2  1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
# Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# 
# Which starting number, under one million, produces the longest chain?
# 
# NOTE: Once the chain starts the terms are allowed to go above one million.
#===============================================================================

startNum = 1000000
endNum = 1
chain = (0,0)

while startNum >= 500000:
    curNum = startNum
    chainLen = 0
    while curNum != endNum:
        chainLen += 1
        if (curNum % 2 == 0):
            curNum = curNum/2
        else:
            curNum = (3 * curNum) + 1
    if (chainLen > int(chain[1])):
        chain = (startNum, chainLen) 
        print chain
    startNum -= 1

print "Starting number with the longest chain is " + `chain[0]` + " of length: " + `chain[1]`