# What is the first number in the Fibonacci sequence that contains 1000 digits?
def fib_digit_counter(n=1000):
    """
    Finds first numer in Fibonacci sequence with n digits
    :param n (int): number of digits
    :return (int): first fib with n digits
    """
    i, j, k, index = 1, 1, 0, 2

    while len(str(j)) < n:
        k = i + j
        i, j = j, k
        index += 1
    
    return index



print(fib_digit_counter())
# Runtime: .033s