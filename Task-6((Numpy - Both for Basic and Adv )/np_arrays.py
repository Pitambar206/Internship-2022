import numpy

def arrays(arr):
    arr.reverse()
    numpy_arr=numpy.array(arr,float)
    return numpy_arr
    # use numpy.array

arr = input().strip().split(' ')
result = arrays(arr)
print(result)