# Mat size must be NXM. (N is an odd natural number, and  M is 3 times .)
# The design should have 'WELCOME' written in the center.
# The design pattern should only use |, . and - characters. 


n,m=input().split()
c='|'
v='.'

n=int(n)
m=int(m)
j=n//2-1
for i in range(n):
    if i==n//2:
        print('WELCOME'.center(m,'-'))
    else:
        if i<n/2:    
            print(((v+c+v)*(2*i+1)).center(m,'-'))
        else:
            print(((v+c+v)*(2*j+1)).center(m,'-'))
            j=j-1
                        