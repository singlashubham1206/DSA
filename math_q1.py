# 1. Missing number in array

# Input:
# N = 5
# A[] = {1,2,3,5}
# Output: 4

# Input:
# N = 10
# A[] = {6,1,2,8,3,4,7,10,5}
# Output: 9


n = 10
arr = [6,1,2,8,3,4,7,10,5]

sum_n = 0
sum_arr = 0

for i in range(1,n+1):
    sum_n = sum_n + i 
    
for i in arr:
    sum_arr += i
    
miss = sum_n - sum_arr

print(miss)
