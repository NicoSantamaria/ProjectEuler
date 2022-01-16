# Find the sum of all multiples of 3 or 5 below 1000
_sum = 0

for x in range(1,1000):
    if (not x % 5) or (not x % 3):
        _sum += x

print(_sum)
# 233168
