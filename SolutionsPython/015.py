# Starting in the top left corner of a 2×2 grid, and only 
# being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?
from math import factorial


def count_lattice_paths(n):
    """
    Counts the number of paths through an nxn grid
    using an optimized form of the choose function
    :param n (int): dimensions of grid
    :return (int): number of paths through grid
    """
    return int(factorial(2 * n) / (factorial(n) ** 2))


print(count_lattice_paths(20))
# 137846528820
# Runtime: 0.034s