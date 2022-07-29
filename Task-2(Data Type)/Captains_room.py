num=int(input())
rooms=(int(x) for x in input().split(' '))
seen={}

for i in rooms:
    if not i in seen:
        seen[i]=1
    else:
        seen[i]+=1
for key,val in seen.items():
    if val !=num:
        print(key)
    