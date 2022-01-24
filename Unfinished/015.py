import timeit
import itertools
start = timeit.default_timer()

paths = set(itertools.permutations(["down", "right"] * 5))
sum = 0
for x in paths:
    if x in paths:
        sum += 1

print(sum)

stop = timeit.default_timer()
print(stop-start)