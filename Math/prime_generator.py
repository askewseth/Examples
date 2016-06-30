"""Sieve of Erathosthenes implementation for random number generation."""

def sieve(n):
    """Sieve of Erathosthenes algorithm."""
    not_prime = []
    prime = []
    for i in xrange(2, n+1):
        if i not in not_prime:
            prime.append(i)
            for j in xrange(i*i, n+1, i):
                not_prime.append(j)
    return prime
