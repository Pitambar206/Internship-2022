# insert i e: Insert e integer  at position i .
# print: Print the list.
# remove e: Delete the first occurrence of integer e .
# append e: Insert integer e at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.

if __name__ == '__main__':
    N = int(input())
    lst=[]
    for i in range(N):
        lst.append(input().split())
    arr=[]
    for i in range(N):
        if lst[i][0]=='insert':
            arr.insert(int(lst[i][1]),int(lst[i][2]))
        elif lst[i][0]=='print':
            print(arr)
        elif lst[i][0]=='remove':
            arr.remove(int(lst[i][1]))
        elif lst[i][0]=='append':
            arr.append(int(lst[i][1]))
        elif lst[i][0]=='pop':
            arr.pop()
        elif lst[i][0]=='sort':
            arr.sort()
        elif lst[i][0]=='reverse':
            arr.reverse()
            
            
