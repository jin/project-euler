#A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,
#a^2 + b^2 = c^2
#For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.


import time, sys
start = time.time()

def main():
    for a in range(1,333):
        b = a + 1
        c = 1000 - a - b
        while (b < c):
            if (a**2 + b**2 == c**2):
                print a*b*c
                print time.time() - start
                sys.exit()
            b+=1
            c-=1
            
main()