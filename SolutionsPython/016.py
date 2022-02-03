# 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 2^1000?
def sum_digit_power(base, exp):
    number = str(base ** exp)
    return sum(int(number[i]) for i in range(len(number)))

sum_digit_power(2, 1000)
# 1366
# Runtime: ~0.000s