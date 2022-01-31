# 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 2^1000?
num = str(2**1000)
sum = 0

for x in range(0, len(num)):
    sum += int(num[x])

print(sum)
# 1366
# Runtime: ~0.000s