import numpy
numpy.set_printoptions(legacy='1.13')
arr=list(map(float,input().split()))
np_arr=numpy.array(arr)
print(numpy.floor(np_arr))
print(numpy.ceil(np_arr))
print(numpy.rint(np_arr))
