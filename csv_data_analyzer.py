import csv

print("=" * 60)
print("              CSV DATA ANALYZER")
print("=" * 60)

students = []

# Read the CSV file
with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        students.append(row)

print(f"\nTotal Students: {len(students)}")


# Calculate subject averages
subjects = ["Physics", "Chemistry", "Mathematics"]

print("\n" + "=" * 60)
print("              SUBJECT AVERAGES")
print("=" * 60)

for subject in subjects:
    marks = [float(student[subject]) for student in students]
    average = sum(marks) / len(marks)

    print(f"{subject:<15}: {average:.2f}")


# Find highest scorer in each subject
print("\n" + "=" * 60)
print("              TOP PERFORMERS")
print("=" * 60)

for subject in subjects:
    top_student = max(
        students,
        key=lambda student: float(student[subject])
    )

    print(
        f"{subject:<15}: "
        f"{top_student['Name']} "
        f"({top_student[subject]} marks)"
    )


# Calculate each student's average
print("\n" + "=" * 60)
print("              STUDENT PERFORMANCE")
print("=" * 60)

student_averages = []

for student in students:
    marks = [
        float(student["Physics"]),
        float(student["Chemistry"]),
        float(student["Mathematics"])
    ]

    average = sum(marks) / len(marks)

    student_averages.append({
        "name": student["Name"],
        "average": average
    })

    print(f"{student['Name']:<12}: {average:.2f}%")


# Find overall top student
top_student = max(
    student_averages,
    key=lambda student: student["average"]
)

print("\n" + "=" * 60)
print("              OVERALL TOP STUDENT")
print("=" * 60)

print(
    f"{top_student['name']} "
    f"with an average of "
    f"{top_student['average']:.2f}%"
)

print("=" * 60)
print("          Analysis completed successfully!")
print("=" * 60)