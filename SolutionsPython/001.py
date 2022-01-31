# Find the sum of all multiples of 3 or 5 below 1000
print(sum(set(range(3, 1000, 3)).union(set(range(5,1000,5)))))
# 233168
# Runtime: ~0.000s
