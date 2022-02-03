# Find the maximum total from top to bottom of the triangle below:
from itertools import product
tri_tuple = tuple([
    [75],
    [95,64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20, 4, 82, 47, 65],
    [19, 1, 23, 75, 3, 34],
    [88, 2, 77, 73, 7, 63, 67],
    [99, 65, 4, 28, 6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
])


def path_sum(path, triangle):
    """
    Uses the param path to sum all the entries of the triangle along
    the path
    :param path (tuple): Binary number representing path through triangle
    :param triangle (tuple): Triangle to be iterated over
    :return (int): Sum of path
    """
    j, path_sum = 0, triangle[0][0]
    
    # Uses binary number path to direct through triangle, summing as it does
    for i in range(1, len(path) + 1):
        j += path[i - 1]
        path_sum += triangle[i][j]

    return path_sum


def sum_comparator(paths, tri):
    """
    Takes the sums of paths through the triangle and returns the highest sum
    :param paths (tuple): All possible paths (n-digit binary numbers)
    :param tri (tuple): Triangle to be iterated over
    :return (int): Max paths sum
    """
    max = 0

    # Finds of each path
    for i in range(len(paths)):
        new_sum = path_sum(paths[i], tri) 

        # Compares to current max
        if new_sum > max:
            max = new_sum

    return max


def max_path_sum(tri):
    """
    Calls sum_comparator to begin problem
    :param tri (tuple): triangle for which highest sum path will be found
    :return (int): Sum of highest sum path
    """
    # Number of steps through path
    n = len(tri) - 1

    # All possible paths through triangle (all n-digit binary numbers)
    path_combinations = tuple(product([0, 1], repeat = n))

    return sum_comparator (path_combinations, tri)


max_path_sum(tri_tuple)
# 1074
# Runtime: 0.041s

"""
NOTES:
There is a more efficient way than brute force to find the max, which involves starting from
the bottom of the triangle and moving upward. I will attempt this solution in problem 67.
"""