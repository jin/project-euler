def divisorGenerator(n):
    """Yield all divisors, excluding n itself"""
    for i in range(1,int(n/2)+1):
        if n % i == 0:
            yield i


def d(n):
    """Return the sum of divisors of a number"""
    divisors = []
    for i in divisorGenerator(n):
        divisors.append(i)
    return sum(divisors)


def amicable(a, b):
    """Check if two numbers are amicable"""
    asum = d(a)
    bsum = d(b)
    if asum == b and bsum == a:
        return True
    else:
        return False


def e_sieve(n):
    """Sieve of Erastrothenes to quicken up computation, since they do not have 
    divisors"""
    candidates = list(range(n + 1))
    end = int (n**0.5)

    for i in xrange(2, end+1):
        if candidates[i]:
            candidates[2*i::i] = [None] * (n//i - 1)
    return [i for i in candidates[2:] if i]


def main():
    """Creates two lists of tuples, (a, d(a)) and (d[d(a)], d(a))"""
    sum = 0
    testvalues = list(range(1,10001))
    primes = e_sieve(10001)
    dlist1 = []
    dlist2 = []
    amicables = []

    for i in testvalues:
        if i in primes:
            testvalues.remove(i)

    for i in testvalues:
        dlist1.append((i, d(i)))

    for j in dlist1:
        dlist2.append((d(j[1]), j[1]))
    
    for i in range(len(dlist1)):
        if dlist1[i] == dlist2[i] and dlist1[i][0] != dlist1[i][1]:
            amicables.append(dlist1[i])
        
    for i in amicables:
        sum += i[0] + i[1]

    print (sum/2)


if __name__ == "__main__":
    main()
