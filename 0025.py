#===============================================================================
# What is the first term in the Fibonacci sequence to contain 1000 digits?
#===============================================================================

import time
start = time.time()

def fib():
    a, b = 1, 1
    while 1:
        yield a
        a, b = b, a + b
        
j = 1
for i in fib():
    if len(str(i)) >= 1000:
        print j
        print time.time() - start
        break
    j += 1