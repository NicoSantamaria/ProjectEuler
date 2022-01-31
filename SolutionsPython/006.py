# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
print(sum(range(1,101))**2 - sum(x**2 for x in range(1,101)))
# 25164150
# Runtime: ~0.000s