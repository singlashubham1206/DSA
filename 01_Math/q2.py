# 2. Trailing zeroes in factorial 

# Input:
# N = 5
# Output:
# 1
# Explanation:
# 5! = 120 so the number of trailing zero is 1

# Input:
# N = 4
# Output:
# 0
# Explanation:
# 4! = 24 so the number of trailing zero is 0.

n = int(input("Enter a number : "))

i = 5 
res = 0

while i <= n:
    res = res + (n//i)
    i *= 5
    
print(res)
