N = int(input())
X = list(map(float,input().strip().split()))
Y = list(map(float,input().strip().split()))

mu_x = sum(X) / N
mu_y = sum(Y) / N

std_x = (sum([(i - mu_x)**2 for i in X]) / N)**0.5
std_y = (sum([(i - mu_y)**2 for i in Y]) / N)**0.5

covariance = sum([(X[i] - mu_x) * (Y[i] - mu_y) for i in range(N)])

correlation_coefficient = covariance / (N * std_x * std_y)

print(round(correlation_coefficient,3))