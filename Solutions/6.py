# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
sumSquares = 0
for x in range(1,101):
    sumSquares += x**2
print(sum(range(1,101))**2 - sumSquares)
# 25164150