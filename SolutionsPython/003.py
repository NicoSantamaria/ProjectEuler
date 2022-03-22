# Find the largest prime factor of 600851475143
def isPrime(num):
    for x in range(2, int(num**0.5)):
        if not num % x:
            return False

    return True


def isFactor(fac, n):
    if not n % fac:
        return True

    return False


def largest_prime_factor(n):
    i = int(n**0.5)

    while not (isPrime(i, n) and isFactor(i, n)):
        i -= 1

    return i


print(largest_prime_factor(600851475143.)) 
# 6857
# Runtime: 1.919s