# What is the first triangle number with over 500 divisors?
def divisorCountCheck(num):
    counter = 0

    for x in range(1, int(num**0.5) + 1):
        if not num % x:
            counter += 2

    return counter > 500

i, tri_num = 1, 1
while not divisorCountCheck(tri_num):
    i += 1
    tri_num += i

print(tri_num)
# 76576500
# Runtime 1.944s