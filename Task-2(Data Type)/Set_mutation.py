# You are given a set A and N number of other sets. These N number of sets have to perform some specific mutation operations on set A.

# Your task is to execute those operations and print the sum of elements from set A .


n=int(input())
A=set(map(int,input().split()))
N=int(input())
for i in range(N):
    cmd=input().split()
    opt=cmd[0]
    S=set(map(int,input().split()))
    if(opt == 'update'):
        A|= S    #Update the set by adding elements from another set.
    elif (opt=='intersection_update'):
        A &= S   #Update the set by keeping only the elements found in it.
    elif(opt=='difference_update'):
        A -= S  #Update the set by removing elements found in another set.
    elif(opt=='symmetric_difference_update') :
        A ^= S  #Update the set by only keeping the elements found in either set, but not in both.
print(sum(A))   
