import math

mean,std = list(map(int,input().split(" ")))
x1 = float(input())
x2 = float(input())

cdf = lambda x: 0.5 * (1 + math.erf((x - mean) / (std * (2 ** 0.5))))

print(round((1-cdf(x1)) * 100 , 2))
print(round((1-cdf(x2)) * 100 , 2))
print(round((cdf(x2)) * 100 , 2))