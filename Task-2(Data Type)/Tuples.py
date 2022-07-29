# Given an integer,n and n space-separated integers as input, create a tuple,t,of those n integers. Then compute and print the result of hash(t).

if __name__ == '__main__':
    n = int(raw_input())
    integer_lst = map(int, raw_input().split())
    t=tuple((integer_lst))
    print(hash(t))