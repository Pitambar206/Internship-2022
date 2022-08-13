import numpy
n,m=map(int,input().split())
np_arr=numpy.array([input().split() for i in range(n)],int)
print(numpy.prod(numpy.sum(np_arr,axis=0),axis=0))



