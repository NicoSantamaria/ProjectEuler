# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
def is_divisible(guess):
    i = 20
    while i > 1:
        if guess % i != 0:
            return False
        i -= 1
    return True

primeBase = 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19
i = primeBase

while is_divisible(i) == False:
    i += primeBase
    
print(i)
# 232792560