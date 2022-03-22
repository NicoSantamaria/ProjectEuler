# Starting in the top left corner of a 2×2 grid, and only 
# being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?
def factorial(n, base=1):
    """
    Factorial down to a given base. Default base is 1.
    :param n (int): number to take factorial of
    :param base=1 (int): bottom multiplier (base)
    :return (int): Factorial from n to base
    """
    if n == base:
        return base

    else:
        return n * factorial(n - 1, base=base)

def count_lattice_paths(n):
    """
    Counts the number of paths through an nxn grid
    using an optimized form of the choose function
    :param n (int): dimensions of grid
    :return (int): number of paths through grid
    """
    return int(factorial(2 * n, n + 1) / factorial(n))


print(count_lattice_paths(20))
# 137846528820
# Runtime: 0.034s

"""
NOTES:
The number of paths through an nxn grid can be expressed by (2n choose n). Some algebra 
simplifies this to the form (n + 1)(n + 2)(...)(n + n)/n! where the top is equal to
2n! down to base case n + 1. To calculate this, I wrote my own recursive factorial function 
with a variable base case. Should be the fastest way to calculate.
"""