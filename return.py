
def get_grade(marks,subject=None):

    if marks<0 or marks>100:
        grade=None
    elif marks<35:
        grade="W"
    elif marks<55:
        grade="S"
    elif marks<65:
        grade="C"
    elif marks<75:
        grade="B"
    else:
        grade="A"

    print("Hello")

    return subject,grade

subject,grade=get_grade(75,"Science")

print(type(grade),grade)

if grade:
    print("Grade = ",grade)
else:
    print("Something went wrong")
