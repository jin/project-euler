# The sum of the squares of the first ten natural numbers is, 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is, (1 + 2 + ... + 10)^2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

import math

def sumOfSquares(first,last):
    sum = 0
    for i in range(first,last):
        sum += math.pow(i,2)
    return sum
        
def squaresOfSum(first,last):
    sum = 0
    for i in range(first,last):
        sum += i
    return math.pow(sum,2)

print int(math.fabs(sumOfSquares(1,101) - squaresOfSum(1,101)))
