# Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
# Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students, order their names alphabetically and print each one on a new line.

if __name__ == '__main__':
    lst=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lst.append([name,score])
    lst.sort(key=lambda lst:lst[1])
    second_lowest=[]
    for i in range(len(lst)):
        if lst[i][1]!=lst[0][1]:
            second_lowest.append(lst[i][0])
            for j in range(i+1,len(lst)):
                if lst[j][1]==lst[i][1]:
                    second_lowest.append(lst[j][0])
                else:
                    break
            break
        else:
            continue
    second_lowest.sort()
    for i in second_lowest:
        print(i)
                    
            
        
        
