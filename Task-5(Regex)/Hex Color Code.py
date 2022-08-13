import re
N=int(input())
for i in range(N):
    matches=re.findall(r':?.(#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3})',input())
    if matches:
        print(*matches,sep='\n')