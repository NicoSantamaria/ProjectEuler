# Find the sum of all the primes below two million.
num = 2000000
numbers = set(range(2, num))
primes = set()

def sieve_multiples(iter, max_num, nums):
    return nums.difference(set(range(iter, max_num, iter)))

i = 2
while i < max(numbers):
    numbers  = sieve_multiples(i, num, numbers)
    primes.add(i)
    i = min(numbers)
    print(i)







# from math import sqrt

# def isPrime(x):
#     for i in range(3, int(sqrt(x))+ 1):
#         if not x % i:
#             return False 
#     return True

# primesSum = 0

# for x in range(1, 2000001, 2):
#     if isPrime(x):
#         primesSum += x

# print(primesSum)
# 142913828922
# Runtime: 11.667s