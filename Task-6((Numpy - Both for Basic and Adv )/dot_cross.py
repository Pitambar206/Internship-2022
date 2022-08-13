import numpy
n=int(input())
np_A=numpy.array([input().split() for i in range(n)],int)
np_B=numpy.array([input().split() for i in range(n)],int)
c=print(numpy.dot(np_A,np_B))

