# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.
def sum_proper_divisors(n):
    """
    Sums the proper divisors of a number
    :param n (int): number
    :return (int): sum of proper divisors
    """
    divisors = {1}
    
    # Finds all proper divisors and adds them to divisor set
    for i in range(2, int(n * 0.5)):
        if not (n / i) % 1:
            divisors.add(n / i)
            divisors.add(i)

    # Returns the sum
    return sum(divisors)


def is_amicable(n):
    """
    Determines if a number is amicable
    :param n (int): number
    :return (Boolean): if the number is amicable
    """
    div_sum = sum_proper_divisors(n)
    div_sum_pair = sum_proper_divisors(div_sum)

    # Return True if n is has an amicable pair which is not itself.
    return (n == div_sum_pair) & (n != div_sum)

        
def sum_amicables(max):
    """
    Finds all amicable numbers up to a maximum, then sums them.
    :param max (int): Maximum possible amicable numbers
    :return (int): Sum of the amicable numbers
    """ 
    amicables = set()

    # Iterates to max and adds all amicable numbers
    for i in range(2, max):
        if is_amicable(i):
            amicables.add(i)
    
    return sum(amicables)


sum_amicables(10000)
# 31626
# Runtime: 2.263s

"""
NOTES:
Not quite at my 2s threshold. Maybe some time to be saved in the
sum_proper_divisors function?
"""
