import re
for i in range(int(input())):
    str=input()
    pattern=re.compile('^[+-]?[0-9]*[.][0-9]+$')
    print(bool(pattern.match(str)))
    