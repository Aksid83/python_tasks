"""
You have a record of N students.
Each record contains the student's name, and their percent marks in Maths, Physics and Chemistry.
The marks can be floating values.
The user enters some integer N followed by the names and marks for N students.
You are required to save the record in a dictionary data type.
The user then enters a student's name.
Output the average percentage marks obtained by that student, correct to two decimal places.

Input Format:
The first line contains the integer N, the number of students.
The next N lines contains the name and marks obtained by that student separated by a space.
The final line contains the name of a particular student previously listed.

Constraints:
2 <= N <= 10
0 <= Marks <= 100

Output Format:
Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.
"""

# 1st solution (bad)
n = int(raw_input())
students = [raw_input().split() for _ in range(n)]
result_student = raw_input()
marksheet = {}
sum_marks = 0
for student in students:
    marksheet[student[0]] = student[1:]
    if student[0] == result_student:
        marks = marksheet[student[0]]
        for mark in marks:
            sum_marks += float(mark)
        result = float(sum_marks)/len(marks)
        print '%.2f' % result

# 2nd solution (best)
n = int(raw_input())
students = {}
for line in range(n):
    info = raw_input().split()
    score = map(float, info[1:])
    students[info[0]] = sum(score) / float(len(score))
print "%.2f" % students[raw_input()]