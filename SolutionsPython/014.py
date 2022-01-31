# The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

collatz_length_dict = {}

def nextCollatz(n):
    if not n % 2:
        return n / 2
    else:
        return 3 * n + 1

def collatzCount(num):
    i = 1
    while num != 1:
        num = nextCollatz(num)

        if num in collatz_length_dict:
            return i + collatz_length_dict[num]
        i += 1
    return i

for x in range(2,1000000):
    collatz_length_dict[x] = collatzCount(x)

print(max(collatz_length_dict, key = collatz_length_dict.get))
# 837799
# Runtime: 1.675