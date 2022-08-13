import numpy
n,m=map(int,input().split())
arr=[]
for i in range(n):
    row=list(map(int,input().split()))
    arr.append(row)
np_arr=numpy.array(arr)
print(numpy.transpose(np_arr))
print(np_arr.flatten())



