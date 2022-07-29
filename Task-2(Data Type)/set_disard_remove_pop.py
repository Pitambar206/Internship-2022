# You have a non-empty set s, and you have to execute N  commands given in N lines.The commands will be pop, remove and discard. 
# Print the sum of the elements of set s on a single line.

n = int(input())
s = set(map(int, input().split()))
for i in range(int(input())):
    c=input().split()
    if c[0]=='pop':
        s.pop()
    elif c=='remove':
        s.remove(int(c[1]))
    else:
        s.discard(int(c[1]))
print(sum(s))