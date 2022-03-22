# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.
import timeit
start = timeit.default_timer()


def sum_proper_divisors(n):
    """
    Sums the proper divisors of a number
    :param n (int): number
    :return (int): sum of proper divisors
    """
    divisor_sum = 1
    
    # Finds all proper divisors and adds them to divisor sum
    for i in range(2, int(n * 0.5)):
        div = n / i
        if not div % 1:
            print(i)
            print(div)
            divisor_sum += i + div

    return divisor_sum


def is_amicable(n):
    """
    Determines if a number is amicable
    :param n (int): number
    :return (Boolean): if the number is amicable
    """
    div_sum = sum_proper_divisors(n)
    div_sum_pair = sum_proper_divisors(div_sum)

    if (n == div_sum_pair) & (n != div_sum):
        return n, div_sum

        
def sum_amicables(max):
    """
    Finds all amicable numbers up to a maximum, then sums them.
    :param max (int): Maximum possible amicable numbers
    :return (int): Sum of the amicable numbers
    """ 
    amicables = set()

    # Iterates to max and adds all amicable numbers
    for i in range(2, max):
        x = is_amicable(i)

        if x:
            amicables.add(x[0])
            amicables.add(x[1])

    return sum(amicables)


print(sum_amicables(10000))
# 31626
# Runtime: 2.263s
stop = timeit.default_timer()
print(stop-start)
"""
NOTES:
I'm double checking amicable numbers. When this algorithm finds
220 and its corresponding amicable number, 284, it adds 220 and continues
iterating upward until it also adds 284. The algorithm could be optimized
by adding 220 and 284 in one go, since the is_amicable function is by far
the most expensive part of the program.
"""