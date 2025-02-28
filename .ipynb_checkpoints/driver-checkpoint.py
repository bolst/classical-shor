import QuantumAlgorithms
import random
from math import gcd

# Shor's algorithm accepts a large integer N and finds p,q such that N=p*q and p,q are both primes
def shor(N: int):

    # choose a random integer between (1,N)
    a = random.randint(2, N-1)

    # compute gcd of a and N
    b = gcd(a, N)

    if b != 1:
        return b, N // b
    else:
        # use quantum subroutine to find the order r of a
        # i.e., min(r > 0) such that a^r = 1 mod N
        r = QuantumAlgorithms.find_order(a, N)

        if r % 2 != 0:
            return shor(N)

        g = gcd(a**(r/2) + 1, N)

        if g > 1:
            return g, N // g
        else:
            return shor(N)