# 3. A Simple Fraction 

# Input: numerator = 1, denominator = 3
# Output: "0.(3)"
# Explanation: 1/3 = 0.3333... So here 3 is recurring.

# Input: numerator = 5, denominator = 2
# Output: "2.5"
# Explanation: 5/2 = 2.5


nr = int(input("Enter numerator : "))
dr = int(input("Enter denomenator : "))

q = nr // dr 
r = nr % dr 

ans = str(q)
dic = {}

if r == 0:
    print(ans)
else:
    ans += '.'
    while r != 0:
        if r in dic.keys():
            ans = ans[:dic[r]] + "(" + ans[dic[r]:] + ")"
            break
        else:
            dic[r] = len(ans)
            r *= 10
            q = r // dr 
            r = r % dr 
            ans += str(q)
            
    print(ans)
