print("=" * 50)
print("       STUDENT RESULT ANALYZER")
print("=" * 50)

name = input("\nEnter student's name: ")

subjects = ["Physics", "Chemistry", "Mathematics", "English", "Computer"]

marks = []

for subject in subjects:
    while True:
        try:
            mark = float(input(f"Enter marks for {subject} (0-100): "))

            if 0 <= mark <= 100:
                marks.append(mark)
                break
            else:
                print("Please enter marks between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")

total = sum(marks)
percentage = total / len(subjects)

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

result = "PASS" if percentage >= 35 else "FAIL"

highest = max(marks)
lowest = min(marks)

highest_subject = subjects[marks.index(highest)]
lowest_subject = subjects[marks.index(lowest)]

print("\n" + "=" * 50)
print("             RESULT SUMMARY")
print("=" * 50)

print(f"Student Name     : {name}")
print(f"Total Marks      : {total:.2f} / 500")
print(f"Percentage       : {percentage:.2f}%")
print(f"Grade            : {grade}")
print(f"Result           : {result}")
print(f"Highest Marks    : {highest:.2f} ({highest_subject})")
print(f"Lowest Marks     : {lowest:.2f} ({lowest_subject})")

print("=" * 50)
print("       Thank you for using the analyzer!")
print("=" * 50)