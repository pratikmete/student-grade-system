 # Student Grade Management System (Pure Python)

students = {}

def add_student():
    """Adds a new student with marks for chosen number of subjects."""
    name = input("Enter student name: ")

    try:
        num_subjects = int(input("Enter number of subjects: "))
        if num_subjects <= 0:
            print("Subjects must be more than 0.\n")
            return
    except ValueError:
        print("Invalid input. Please enter a valid number.\n")
        return

    try:
        # Enter marks in one line → e.g., 80 75 90
        marks = list(map(int, input(f"Enter marks for {num_subjects} subjects (space-separated): ").split()))
        if len(marks) != num_subjects:
            print(f"Please enter exactly {num_subjects} marks.\n")
            return
    except ValueError:
        print("Invalid input. Please enter numbers only.\n")
        return

    students[name] = marks
    print("✅ Student added successfully!\n")


def view_students():
    """Displays all students with total, average, and grade."""
    if not students:
        print("No student records found.\n")
        return

    for name, marks in students.items():
        total = sum(marks)
        avg = total / len(marks)

        # Simple grading system
        if avg >= 75:
            grade = "A"
        elif avg >= 50:
            grade = "B"
        else:
            grade = "C"

        print(f"Name: {name}, Marks: {marks}, Total: {total}, Avg: {avg:.2f}, Grade: {grade}")


def topper():
    """Finds and displays the student with the highest total marks."""
    if not students:
        print("No students yet.\n")
        return

    top_student = max(students, key=lambda x: sum(students[x]))
    print(f"🏆 Topper: {top_student} with {sum(students[top_student])} marks.\n")


# Main menu
while True:
    print("\n--- Student Grade Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Show Topper")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        topper()
    elif choice == "4":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice, try again.\n")

