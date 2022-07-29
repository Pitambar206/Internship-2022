# Print the average of the marks array for the student name provided, showing 2 places after the decimal.

if __name__ == '__main__':
    n = int(input()) #The number of students'
    student_marks = {} #Marks key:value pairs
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input() #The name of a student to query.
    marks=0
    for i in student_marks[query_name]:
        marks=marks+i
    avg=marks/3         #Average 
    print("%0.2f"%avg)   # The average of the marks obtained by the particular student correct to 2 decimal places.
 