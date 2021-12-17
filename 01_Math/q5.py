# 5. Smallest Positive Integer that can not be represented as Sum

# Input: 
# N = 6
# array[] = {1, 10, 3, 11, 6, 15}
# Output: 
# 2
# Explanation:
# 2 is the smallest integer value that cannot 
# be represented as sum of elements from the array.


# Input: 
# N = 3
# array[] = {1, 1, 1}
# Output: 
# 4
# Explanation: 
# 1 is present in the array. 
# 2 can be created by combining two 1s.
# 3 can be created by combining three 1s.
# 4 is the smallest integer value that cannot be 
# represented as sum of elements from the array.

arr = [1,2,4]
res = 1

arr.sort()

for i in range (0,len(arr)):
    if arr[i] <= res:
        res = res + arr[i]
    else:
        break

print(res)
