# Find the sum of the digits in the number 100!
from math import factorial


def sum_factorial_digits(num):
    """
    Sums digits of n!
    :param num (int): Base of factorial
    :return (int): Sum of digits
    """
    num_string = str(factorial(num))
    return sum(int(num_string[i]) for i in range(len(num_string)))


sum_factorial_digits(100)
# 648
# Runtime: 0.000s