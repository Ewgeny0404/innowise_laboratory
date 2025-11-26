
students = []  # global list of students and their grades


def add_students(students):
    """
    add a new student to the students list if they don't already exist

    function asks the user for a student's name and then checks
    if this name is already exist in the students list
    """
    name = input("Enter student's name: ")
    name = name.strip()  # remove left and right spaces

    # check if a student with this name already exists
    for student in students:
        if student["name"] == name:
            print("Student already exist.")
            return

    # if we didn't return inside the loop, this is a new student
    students.append({"name": name, "grades": []})


def add_grades(students):
    """
    add grades for an existing student

    the function ask for a student's name and finds the matching student,
    and then repeatedly ask for grades until the user types 'done'
    it validates that each grade is a number from 0 to 100
    """
    name = input("Enter student's name: ")
    name = name.strip()

    # try to find the student with the given name
    for student in students:
        if student["name"] == name:
            # if we found the student we can start asking for grades
            while True:
                grade = input("Enter a grade (or 'done' to finish): ")

                # exit from grades input loop
                if grade.lower() == "done":
                    break

                try:
                    grade = int(grade)
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    continue

                # check that the grade is in the allowed range
                if 0 <= grade <= 100:
                    student["grades"].append(grade)
                else:
                    print("Invalid input. Please enter a number from 0 to 100.")
            return

    # if we exit the loop without return, student was not found
    print("Student not found.")


def show_report(students):
    """
    show a report for all students

      if there are no grades, prints n/a
      else, prints the average grade

      if there are any valid averages, prints max, min, and overall average
      if there are no grades, prints 'no grades available'
    """
    if not students:
        print("No students yet")
        return
    else:
        averages = []  # collect averages for summary at the end

        for student in students:
            grades = student["grades"]

            # if the student has no grades, we show n/a and continue
            if not grades:
                print(f"{student['name'].title()}'s average grade is N/A.")
                print(26 * "-")
                continue

            # handle possible ZeroDivisionError
            try:
                student_average = sum(grades) / len(grades)
            except ZeroDivisionError:
                print(f"{student['name'].title()}'s average grade is N/A")
            else:
                averages.append(student_average)
                print(f"{student['name'].title()}'s average grade is {student_average}")
            print(26 * "-")

        # if we dont have any averages, it means there were no grades
        if not averages:
            print("No grades available.")
            return

        # max, min and overall average
        print(f"Max Average: {max(averages)}")
        print(f"Min Average: {min(averages)}")
        print(f"Overall Average: {sum(averages) / len(averages)}")


def find_top_performer(students):
    """
    print the top performer based on the highest average grade

      ignores students without grades.
      uses max() with a key function (average) to find the best student
      prints a message if there are no students or no grades
    """
    if not students:
        print("No students added yet.")
        return

    # we only consider students that actually have grades
    valid_students = [s for s in students if s["grades"]]

    if not valid_students:
        print("No grades have been added yet.")
        return

    def average(grades):
        """
        helpe-function to calculate the average of a list of grades

        return 0 if there is a ZeroDivisionError
        """
        try:
            return sum(grades) / len(grades)
        except ZeroDivisionError:
            return 0

    # max() will use our average() function to compare students by their average grade
    top_student = max(valid_students, key=lambda s: average(s["grades"]))
    top_avg = average(top_student["grades"])

    print(
        f"Top performer is {top_student['name'].title()} "
        f"with an average grade of {top_avg:.1f}."
    )


def show_menu():
    """
    print the main menu

    this function just shows the list of available options
    """
    print("""
--- Student Grade Analyzer ---
1. Add a new student
2. Add grades for a student
3. Show report
4. Find top performer
5. Exit
""")


def main():
    """
    main loop of the program

    shows the menu, reads the user's choice,
    and calls the corresponding function
    """
    while True:
        show_menu()

        try:
            choise = int(input())
        except ValueError:
            print("Invalid input.")
            continue

        # using match-case to handle menu options
        match choise:
            case 1:
                add_students(students)
            case 2:
                add_grades(students)
            case 3:
                show_report(students)
            case 4:
                find_top_performer(students)
            case 5:
                break
            case _:
                print("Invalid choise.")


if __name__ == "__main__":
    # this ensures main() only runs when the script is executed directly
    main()
