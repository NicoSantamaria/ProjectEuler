# Find the largest prime factor of 600851475143
from math import sqrt

number = 600851475143.
factor = int(sqrt(number))

def isPrime(x):
    for i in range(2, int(sqrt(x)) + 1):
        if not x % i:
            return False 
    return True

def isFactor(y):
    return not (number / y ) % 1

while factor > 1:
    if isFactor(factor) and isPrime(factor):
        print(factor)
        break
    factor -= 1
# 6857
