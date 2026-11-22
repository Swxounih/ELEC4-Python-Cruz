
import student_utils
from student_utils import calculate_average
from datetime import datetime

grades = []

print("================================")
print("       STUDENT GRADE REPORT")
print("================================")

name = input("Enter student name: ")

number_of_subjects = int(input("Enter number of subjects: "))

for i in range(number_of_subjects):
    grade = float(input(f"Enter grade for subject {i + 1}: "))
    grades.append(grade)

# Using imported functions
average = calculate_average(grades)
status = student_utils.determine_status(grades)
highest = student_utils.get_highest_grade(grades)
lowest = student_utils.get_lowest_grade(grades)

# Using built-in datetime module
report_date = datetime.now()

print("\n================================")
print("          GRADE REPORT")
print("================================")

print(f"Student Name: {name}")
print(f"Average Grade: {average:.2f}")
print(f"Highest Grade: {highest:.2f}")
print(f"Lowest Grade: {lowest:.2f}")
print(f"Status: {status}")

print("--------------------------------")
print("Report Generated:")
print(report_date.strftime("%B %d, %Y %I:%M %p"))
print("================================")
