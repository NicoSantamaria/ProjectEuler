# Find the largest prime factor of 600851475143
def isPrime(num):
    for x in range(2, int(num**0.5)):
        if not num % x:
            return False

    return True


def isFactor(fac):
    if not number % fac:
        return True

    return False


def largest_prime_factor(n):
    i = int(number**0.5)

    while not (isPrime(i) and isFactor(i)):
        i -= 1

    return i


print(largest_prime_factor(600851475143.)) 
# 6857
# Runtime: 1.919s