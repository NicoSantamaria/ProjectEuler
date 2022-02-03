# import timeit
# start = timeit.default_timer()

# def sum_proper_divisors(n):
#     """
#     Sums the proper divisors of a number
#     :param n (int): number
#     :return (int): sum of proper divisors
#     """
#     divisors = {1}
    
#     # Finds all proper divisors and adds them to divisor set
#     for i in range(2, int(n * 0.5)):
#         if not (n / i) % 1:
#             divisors.add(n / i)
#             divisors.add(i)

#     # Returns the sum
#     return sum(divisors)

# def is_amicable(n):
#     """
#     Determines if a number is amicable
#     :param n (int): number
#     :return (Boolean): if the number is amicable
#     """
#     div_sum = sum_proper_divisors(n)
#     div_sum_pair = sum_proper_divisors(div_sum)

#     return (n == div_sum_pair) & (n != div_sum), int(div_sum)

        
# def sum_amicables(max):
#     """
#     Finds all amicable numbers up to a maximum, then sums them.
#     :param max (int): Maximum possible amicable numbers
#     :return (int): Sum of the amicable numbers
#     """ 
#     amicables = dict(zip((i for i in range(max)), [None] * max))

#     # Iterates to max and adds all amicable numbers
#     for i in range(max):
#         if amicables[i] is None:
#             result = is_amicable(i)
#             amicables[i], amicables[result[1]] = result[0], result[0]

#     print(amicables)
#     print(list(amicables.keys())[list(amicables.values()).index(True)])
#     return list(amicables.keys())[list(amicables.values()).index(True)]

        

# sum_amicables(500)
# # 31626
# # Runtime: 2.577s

# stop = timeit.default_timer()
# print(stop - start)
def sum_proper_divisors(n):
    """
    Sums the proper divisors of a number
    :param n (int): number
    :return (int): sum of proper divisors
    """
    divisors = {1}
    
    # Finds all proper divisors and adds them to divisor set
    for i in range(2, int(n * 0.5)):
        if not (n / i) % 1:
            divisors.add(n / i)
            divisors.add(i)

    # Returns the sum
    return sum(divisors)

def is_amicable(n):
    """
    Determines if a number is amicable
    :param n (int): number
    :return (Boolean): if the number is amicable
    """
    div_sum = sum_proper_divisors(n)
    div_sum_pair = sum_proper_divisors(div_sum)

    return (n == div_sum_pair) & (n != div_sum), int(div_sum)


def add_amicable(num, am_list):
    if am_list[num] is not None:
        return am_list

    result = is_amicable(num)
    am_list[num] = result[0]

    if result[1] < len(am_list):
        am_list[result[1]] = result[0]

    return am_list

max = 10000
amicables = [None] * max 

def func(max, amicables):
    for i in range(max):
        amicables = add_amicable(i, amicables)

    return amicables

amicables = func(max, amicables)

sum_ = 0
for i in range(len(amicables)):
    if amicables[i]:
        sum_ += i


