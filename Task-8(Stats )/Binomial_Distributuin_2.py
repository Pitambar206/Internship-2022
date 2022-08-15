import math
p,res = 0.12,0
for i in range(0, 3):
    res+= math.factorial(10)/math.factorial(i)/math.factorial(10-i) * p**i * (1-p)**(10-i)
    if i == 1:
        ans = 1-res
print(round(res, 3))
print(round(ans, 3))