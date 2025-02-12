def get_top_student(subject: str, dataset: dict):
    max_marks = 0
    max_student = ""

    for name, marks in dataset.items():
        if max_marks < marks:
            max_marks = marks
            max_student = name

    return max_student, max_marks


def get_marks(record: tuple):
    return record[1]


# Read file contents
with open('student_marks_details.txt') as file:
    lines = file.readlines()  # Read all lines into a list

# Check if the file is empty
if not lines:
    print("Something went wrong: File is empty")
    exit()

marks_lines = lines[1:]  # Skip the header line

subject_marks = {}
student_marks = {}  # Initialize student marks dictionary
messages = []  # Initialize messages list

# Process each line
for line in marks_lines:
    line = line.strip()

    # Skip empty lines
    if not line:
        continue

    entries = line.split(',')

    # Ensure the line has at least 3 values (name, subject, marks)
    if len(entries) < 3:
        print(f"Skipping invalid line (not enough values): {line}")
        continue

    name = entries[0].strip()
    subject = entries[1].strip()

    try:
        marks = int(entries[2].strip())  # Convert marks to integer
    except ValueError:
        print(f"Skipping line with invalid marks: {line}")
        continue

    # Store marks for each subject
    if subject not in subject_marks:
        subject_marks[subject] = {}

    subject_marks[subject][name] = marks

    # Store total marks for each student
    prev_marks = student_marks.get(name, 0)
    student_marks[name] = prev_marks + marks

# Find top student for each subject
for subject, dataset in subject_marks.items():
    name, marks = get_top_student(subject, dataset)
    msg = f"Top student for {subject} is {name} with {marks} marks"
    print(msg)
    messages.append(msg)

# Find overall top student
marks_list = [(name, marks) for name, marks in student_marks.items()]
marks_list.sort(key=get_marks, reverse=True)

if marks_list:
    top = marks_list[0]
    msg = f"Top student overall is {top[0]} with {top[1]} marks."
    messages.append(msg)
    print(msg)

# Write results to file
with open('results.txt', 'w') as output_file:
    for msg in messages:
        output_file.write(msg + '\n')
