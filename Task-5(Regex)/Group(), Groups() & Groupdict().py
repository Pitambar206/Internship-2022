import re
m=input()
regex=r'([a-z0-9A-Z])\1+'
a=re.search(regex,m)
if a:
    print(a.group(1))
else:
    print(-1)