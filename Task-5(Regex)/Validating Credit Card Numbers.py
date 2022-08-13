import re
for i in range(int(input())):
    s=input().strip()
    pre_match=re.search(r'^[456]\d{3}(-?)\d{4}\1\d{4}\1\d{4}$',s)
    if pre_match:
        proceed_string="".join(pre_match.group(0).split('-'))
        final_match=re.search(r'(\d)\1{3,}',proceed_string)
        if final_match:
            print('Invalid')
        else:
            print('Valid')
    else:
        print('Invalid')
            