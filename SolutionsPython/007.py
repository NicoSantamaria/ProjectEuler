# What is the 10,001st prime number?
def isPrime(x):
    for i in range(2, int(x**0.5)+ 1):
        if not x % i:
            return False 
    
    return True


def find_nprime(n):
    i, j = 1, 0

    while j < n:
        i += 1  

        if isPrime(i):
            j += 1

    return i
    

print(find_nprime(10001))
# 104743
# Runtime: 0.229s