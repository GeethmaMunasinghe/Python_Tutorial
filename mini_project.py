lines= None
with open('student_marks_details.txt')as file:
    lines=file.readline()

if not lines:
    print("Something went wrong")
    exit()

marks_lines=lines[1:]

for line in marks_lines:
    entries=line.split(',')

