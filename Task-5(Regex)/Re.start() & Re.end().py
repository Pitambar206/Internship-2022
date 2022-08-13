import re 
string=input()
sub_str=input()
m=re.finditer(r'(?=(' + sub_str + '))',string)
match=False
for i in m:
    match=True
    print((i.start(1),i.end(1)-1))
if match==False:
    print((-1,-1))
