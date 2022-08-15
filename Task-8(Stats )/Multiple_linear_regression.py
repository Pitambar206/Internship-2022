from sklearn import linear_model

m,n = [int(x) for x in input().strip().split(' ')]
d = [[float(x) for x in input().strip().split(' ')] for i in range(n)]

N= int(input().strip())
inp = [[float(x) for x in input().strip().split(' ')] for i in range(N)]

x = [[d[j][i] for i in range(m)] for j in range(n)]
y = [ d[j][m] for j in range(n)]

lm = linear_model.LinearRegression()
lm.fit(x,y)

a = lm.intercept_
b = lm.coef_

res = [a + sum([b[i] * inp[j][i] for i in range(m)]) for j in range(N)]
for y in res:
    print(y)