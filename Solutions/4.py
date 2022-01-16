# Find the largest palindrome that is the product of two 3-digit numbers
palindrome = 0

for x in range(999, 100, -1):
    for y in range(999, 100, -1):
        if str(x * y) == str(x * y)[::-1] and x * y > palindrome:
            palindrome = x * y

print(palindrome)
# 906609