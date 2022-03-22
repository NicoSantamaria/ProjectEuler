# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For 
# example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 
# 28 is a perfect number.

# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant 
# if this sum exceeds n.

# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written 
# as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers 
# greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot 
# be reduced any further by analysis even though it is known that the greatest number that cannot be expressed 
# as the sum of two abundant numbers is less than this limit.

# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
import timeit
start = timeit.default_timer()


def is_abundant(n):
    """
    Sums the proper divisors of a number
    :param n (int): number
    :return (bool): if sum of proper divisors greater than n
    """
    divisors = {1}
    
    # Finds all proper divisors and adds them to divisor set
    for i in range(2, int(n * 0.5)):
        if not (n / i) % 1:
            divisors.add(n / i)
            divisors.add(i)

    # Returns if sum is greater than n
    return sum(divisors) > n


def is_sum_of_abundants(n, nums):
    """
    Determines if a number is the sum of two other numbers in a tuple,
    :param n (int): desired sum
    :param nums (tuple): numbers to be combined
    :return (bool): if n is a sum of two elements of num
    """
    for num1 in nums:
        for num2 in nums:

            # Check every combination and return True if it sums
            if n == num1 + num2:
                return True

    # Else return False
    return False


def gen_abundant_nums(maximum):
    """
    Generates a tuple of abundant numbers up
    to a given maximum.
    :param maximum (int): maximum possible abundant number
    :return (tuple): tuple of abundant numbers
    """
    abundant_nums = set()

    # Iterate from smallest abundant num, 12, to max
    for i in range(12, maximum + 1):

        # If abundant, add to set
        if is_abundant(i):
            abundant_nums.add(i)
    
    # Change set to tuple and return
    return tuple(abundant_nums)


def sum_of_not_abundant_combinations(maximum=28123):
    """
    Finds the sum of all the positive integers which
    cannot be written as the sum of two abundant numbers.
    :param maximum (int): maximum possible abundant number which cannot
    be summed to a number less than 28123
    :return (int): Sum of all positive integers which cannot be written as
    the sum of two abundant numbers
    """

    # Generate abundant numbers
    abundants = gen_abundant_nums(maximum // 2 + 1)
    _sum = 0

    # Sum numbers which can be expressed as the sum of two abundants
    for i in range(24, maximum):
        if not is_sum_of_abundants(i, abundants):
            _sum += i
    
    return i


stop = timeit.default_timer
print(sum_of_not_abundant_combinations())

print(stop-start)