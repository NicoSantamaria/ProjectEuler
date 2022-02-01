# Find the sum of the digits in the number 100!
from math import factorial

num = str(factorial(100))
print(sum(int(num[i]) for i in range(len(num))))
# 648
# Runtime: 0.000s