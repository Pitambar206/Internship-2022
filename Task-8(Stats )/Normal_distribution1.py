import math
def solve(x, mean, std):
    return 1/2*(1+math.erf((x-mean) / std / 2**(1/2)))
mean = 20
std = 2
print(round(solve(19.5, mean, std), 3))
print(round(solve(22, mean, std) - solve(20, mean, std), 3))