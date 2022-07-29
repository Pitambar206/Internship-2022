# You are given two sets,A and B.Your job is to find whether set A is a subset of set B .

# If set A is subset of set B, print True.
# If set A is not a subset of set B , print False.

for i in range(int(input())):
    a=int(input())
    A=set(input().split())
    b=int(input())
    B=set(input().split())
    print(A.issubset(B))