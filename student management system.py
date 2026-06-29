# ==========================================
# Student Management System
# Python Mini Project
# ==========================================

students = {}


# ------------------------------------------
# Calculate Percentage and Grade
# ------------------------------------------
def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B+"
    elif percentage >= 60:
        return "B"
    elif percentage >= 50:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "Fail"


# ------------------------------------------
# Add Student
# ------------------------------------------
def add_student():
    try:
        roll = int(input("Enter Roll Number : "))

        if roll in students:
            print("Roll number already exists.")
            return

        name = input("Enter Name : ")

        marks = []
        total = 0

        print("Enter Marks of 5 Subjects")

        for i in range(5):
            while True:
                try:
                    mark = float(input(f"Subject {i+1}: "))
                    if mark < 0 or mark > 100:
                        print("Marks must be between 0 and 100.")
                    else:
                        marks.append(mark)
                        total += mark
                        break
                except ValueError:
                    print("Invalid input.")

        percentage = total / 5
        grade = calculate_grade(percentage)

        students[roll] = {
            "name": name,
            "marks": marks,
            "percentage": percentage,
            "grade": grade
        }

        print("\n=== Record Added Successfully ===")
        print(f"Name : {name}")
        print(f"Roll : {roll}")
        print(f"Percentage : {percentage:.2f}%")
        print(f"Grade : {grade}")

    except ValueError:
        print("Invalid Roll Number.")


# ------------------------------------------
# View All Students
# ------------------------------------------
def view_all():
    if len(students) == 0:
        print("No student records found.")
        return

    print("\n")
    print("-" * 75)
    print("{:<10}{:<20}{:<20}{:<10}{:<10}".format(
        "Roll", "Name", "Marks", "%", "Grade"))
    print("-" * 75)

    for roll, data in students.items():
        marks = ",".join(str(int(m)) for m in data["marks"])

        print("{:<10}{:<20}{:<20}{:<10.2f}{:<10}".format(
            roll,
            data["name"],
            marks,
            data["percentage"],
            data["grade"]
        ))

    print("-" * 75)


# ------------------------------------------
# Search Student
# ------------------------------------------
def search_student():
    try:
        roll = int(input("Enter Roll Number : "))

        if roll in students:
            s = students[roll]

            print("\nStudent Details")
            print("------------------------")
            print("Name :", s["name"])
            print("Roll :", roll)
            print("Marks :", s["marks"])
            print("Percentage :", f"{s['percentage']:.2f}%")
            print("Grade :", s["grade"])

        else:
            print("Student not found.")

    except ValueError:
        print("Invalid Roll Number.")


# ------------------------------------------
# Update Student
# ------------------------------------------
def update_student():
    try:
        roll = int(input("Enter Roll Number : "))

        if roll not in students:
            print("Student not found.")
            return

        s = students[roll]

        print("Leave blank if no change.")

        name = input(f"Enter New Name ({s['name']}): ")

        if name != "":
            s["name"] = name

        choice = input("Update Marks? (y/n): ")

        if choice.lower() == "y":
            marks = []
            total = 0

            for i in range(5):
                while True:
                    try:
                        mark = float(input(f"Subject {i+1}: "))
                        if mark < 0 or mark > 100:
                            print("Marks should be between 0-100.")
                        else:
                            marks.append(mark)
                            total += mark
                            break
                    except ValueError:
                        print("Invalid input.")

            percentage = total / 5
            grade = calculate_grade(percentage)

            s["marks"] = marks
            s["percentage"] = percentage
            s["grade"] = grade

        print("Record Updated Successfully.")

    except ValueError:
        print("Invalid Roll Number.")


# ------------------------------------------
# Delete Student
# ------------------------------------------
def delete_student():
    try:
        roll = int(input("Enter Roll Number : "))

        if roll not in students:
            print("Student not found.")
            return

        confirm = input("Delete this record? (y/n): ")

        if confirm.lower() == "y":
            del students[roll]
            print("Record Deleted Successfully.")
        else:
            print("Deletion Cancelled.")

    except ValueError:
        print("Invalid Roll Number.")


# ------------------------------------------
# Show Menu
# ------------------------------------------
def show_menu():
    print("\n")
    print("=" * 40)
    print("   STUDENT MANAGEMENT SYSTEM")
    print("=" * 40)
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")


# ------------------------------------------
# Main Program
# ------------------------------------------
while True:
    show_menu()

    try:
        choice = int(input("Enter Your Choice : "))

        if choice == 1:
            add_student()

        elif choice == 2:
            view_all()

        elif choice == 3:
            search_student()

        elif choice == 4:
            update_student()

        elif choice == 5:
            delete_student()

        elif choice == 6:
            print("Thank You!")
            break

        else:
            print("Invalid Choice.")

    except ValueError:
        print("Please enter a valid number.")