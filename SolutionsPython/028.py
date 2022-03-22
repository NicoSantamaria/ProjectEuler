# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13

# It can be verified that the sum of the numbers on the diagonals is 101.

# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
def sum_diagonals(n):
    """
    Starting from outermost square, sums the four corners then moves inward.
    :param n (int): dimensions of spiral
    :return (int): sum of diagonals
    """

    # Base case
    if n == 1:
        return 1

    else:

        # Sums the corners than moves one square inward
        corners = n ** 2 + (n ** 2 - (n - 1)) + (n ** 2 -  2 * (n - 1)) + (n ** 2 - 3 * (n - 1))
        return corners + sum_diagonals(n - 2)


print(sum_diagonals(1001))
# 669171001
# Runtime: 0.001s

""""
NOTES:
This one's very efficient. Comes from the insight that the sum of the corners of 
the n-th wide square within the spiral is equal to:
n ** 2 + (n ** 2 - (n - 1)) + (n ** 2 -  2 * (n - 1)) + (n ** 2 - 3 * (n - 1))
Then it's just a matter of summing all the square shells within the spiral
"""
