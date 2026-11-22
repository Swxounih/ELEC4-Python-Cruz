
# p1_grade_calculator.py


grades = []


# 1. Accept student's grades
def accept_grades():
    grades.clear()

    print("\n--- Enter Student Grades ---")

    while True:
        try:
            numberOfGrades = int(input("How many grades will you enter? "))

            if numberOfGrades > 0:
                break
            else:
                print("Please enter a number greater than 0.")

        except ValueError:
            print("Invalid input. Please enter a whole number.")

    for i in range(numberOfGrades):
        while True:
            try:
                grade = float(input(f"Enter grade {i + 1}: "))

                if grade >= 0 and grade <= 100:
                    grades.append(grade)
                    break
                else:
                    print("Grade must be from 0 to 100.")

            except ValueError:
                print("Invalid input. Please enter a number.")


# 2. Compute average
def compute_average(grades):
    return sum(grades) / len(grades)


# 3. Get highest grade
def get_highest_grade(grades):
    return max(grades)


# 4. Get lowest grade
def get_lowest_grade(grades):
    return min(grades)


# 5. Determine pass or fail
def determine_status(grades):
    PASSING_GRADE = 75
    if compute_average(grades) >= PASSING_GRADE:
        return "PASSED"
    else:
        return "FAILED"


# 6. Display results
def view_results():
    if len(grades) == 0:
        print("\nNo grades entered yet.")
    else:
        print("\n--- GRADE RESULTS ---")
        print("Grades:", grades)
        print("Average:", round(compute_average(grades), 2))
        print("Highest Grade:", get_highest_grade(grades))
        print("Lowest Grade:", get_lowest_grade(grades))
        print("Status:", determine_status(grades))


# 7. Main menu
def main():
    while True:
        print("\n===== GRADE CALCULATOR =====")
        print("1. Enter Grades")
        print("2. View Results")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            accept_grades()

        elif choice == "2":
            view_results()

        elif choice == "3":
            print("Thank you for using the program!")
            break

        else:
            print("Invalid choice. Please try again.")


main()


# Local vs. Global Variables:
# A global variable is declared outside a function and can be accessed
# by different functions. In this program, grades is a global variable.
# A local variable is declared inside a function and can only be used
# within that function. For example, num is a local variable inside
# accept_grades().
