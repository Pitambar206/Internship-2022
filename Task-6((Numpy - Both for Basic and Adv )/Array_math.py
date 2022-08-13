import numpy
n,m=map(int,input().split())
A=numpy.array([list(map(int,input().split()))for i in range(n)])
B=numpy.array([list(map(int,input().split()))for i in range(n)])
print(A+B)
print(A-B)
print(A*B)
print(A//B)
print(A%B)
print(A**B)





