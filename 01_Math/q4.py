# 4. Nth Natural Number

# Input:
# N = 8
# Output:
# 8
# Explanation:
# After removing natural numbers which contains
# digit 9, first 8 numbers are 1,2,3,4,5,6,7,8
# and 8th number is 8.

# Input:
# N = 9
# Output:
# 10
# Explanation:
# After removing natural numbers which contains
# digit 9, first 9 numbers are 1,2,3,4,5,6,7,8,10
# and 9th number is 10.

n = int(input("Enter a number : "))

pos = 1
res = 0

while n > 0:
    r = n % 9
    n = n // 9
    res = res + (r*pos)
    pos = pos * 10
    
print(res)
