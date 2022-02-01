# 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 2^1000?
number = str(2**1000)
print(sum(int(number[i]) for i in range(len(number))))
# 1366
# Runtime: ~0.000s