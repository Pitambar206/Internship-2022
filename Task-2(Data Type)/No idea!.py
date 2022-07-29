n,m=map(int,input().split())
c=list(map(int,input().split())) #take input elements list
A=set(map(int,input().split()))
B=set(map(int,input().split()))
count=0  #initially count as 0
for i in c:
    if i in A:
        count+=1
    if i in B:
        count-=1
print(count)
        
