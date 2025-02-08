
def get_grade(subject,marks):
    print("Subject = ",subject)
    if marks<0 or marks>100:
        print("Invalid")
    elif marks<35:
        print("W")
    elif marks<55:
        print("S")
    elif marks<65:
        print("C")
    elif marks<75:
        print("B")
    else:
        print("A")

get_grade("English",75)
get_grade("Maths",34)