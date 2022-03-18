# Find the largest palindrome that is the product of two 3-digit numbers
def palindrome_product():
    palindrome = 0

    for x in range(999, 100, -1):
        for y in range(999, 100, -1):
            if str(x * y) == str(x * y)[::-1] and x * y > palindrome:
                palindrome = x * y
    
    return palindrome


print(palindrome_product())
# 906609
# Runtime: 0.031s