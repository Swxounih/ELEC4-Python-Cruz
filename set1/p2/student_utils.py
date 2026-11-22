PASSING_GRADE = 75


def calculate_average(grades):
    return sum(grades) / len(grades)


def determine_status(grades):
    if calculate_average(grades) >= PASSING_GRADE:
        return "PASSED"
    else:
        return "FAILED"


def get_highest_grade(grades):
    return max(grades)


def get_lowest_grade(grades):
    return min(grades)
