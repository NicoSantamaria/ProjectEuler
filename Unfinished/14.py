import timeit
start = timeit.default_timer()

def nextCollatz(n):
    if not n % 2:
        return n / 2
    else:
        return 3 * n + 1

def collatzCount(num):
    i = 1
    while nextCollatz(num) != 1:
        num = nextCollatz(num)
        i += 1
    return i + 1

max = 0
for x in range(1, 1000000):
    if collatzCount(x) > max:
        max = x

print(max)

stop = timeit.default_timer()
print(stop- start)