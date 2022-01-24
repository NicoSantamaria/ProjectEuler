# Find the largest prime factor of 600851475143
number = 600851475143.
factor = int(number**0.5)

def isPrimeFactor(x):
    if not (number / x) % 1:
        for i in range(2, int(x**0.5) + 1):
            if not x % i:
                return False
            return True
    return False

while factor > 1:
    if isPrimeFactor(factor):
        print(factor)
        break
    factor -= 1
# 6857
