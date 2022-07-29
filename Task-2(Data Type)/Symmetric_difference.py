a=int(input())
A=set(map(int,input().split(' ')))
b=int(input())
B=set(map(int,input().split(' ')))
A_set=set(A)
B_set=set(B)
temp_A=A_set.difference(B_set)
temp_B=B_set.difference(A_set)
result=temp_A.union(temp_B)
result=sorted(result)

for i in result:
    print(i)
    