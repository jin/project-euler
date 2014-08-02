#===============================================================================
# The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
# 
# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
#===============================================================================

import time

def expoGen():
    x = 1
    while x<=1000:
        yield (x**x)
        x+=1
        
def directAddition():
    sumOf = 0        
    for i in expoGen():
        sumOf += i
    return sumOf
    
def listAppend():
    list = []
    for i in expoGen():
        list.append(i)
    return list

print directAddition.__name__
start = time.time()
print str(directAddition())[-10:]
print time.time() - start

print ""
print listAppend.__name__
start = time.time()
print (str(sum(listAppend())))[-10:]
print time.time() - start
