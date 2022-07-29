# You are given a set A  and N other sets.
Your job is to find whether set A is a strict superset of each of the N sets.Print True, if A is a strict superset of each of the n sets. Otherwise, print False.

# A strict superset has at least one element that does not exist in its subset.

A=set(input().split())
ans=True
for i in range(int(input())):
    N=set(input().split())
    if (A > N)==False:
        ans=False
        break
print(ans)
