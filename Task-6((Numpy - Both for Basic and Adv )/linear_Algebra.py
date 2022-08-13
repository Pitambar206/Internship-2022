import numpy
n=int(input())
A=numpy.array([input().split() for i in range(n)],float)
print(round(numpy.linalg.det(A),2))

