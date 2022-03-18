# Find the sum of all the even numbers in the Fibonacci series not exceeding 4,000,000
def fib_even_sum(n):
    i, j, k, _sum = 1, 1, 0, 0

    while k <= n:
        if not k % 2:
            _sum += k
        i, j = j, k
        k = i + j


print(fib_even_sum(4000000))
# 4613732
# Runtime: 0.022s