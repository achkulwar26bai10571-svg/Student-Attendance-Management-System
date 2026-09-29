# Student Attendance Management System

students = {}


def add_student():
    roll = input("Enter roll number: ")
    name = input("Enter student name: ")

    if roll in students:
        print("Student already exists.")
        return

    students[roll] = {
        "name": name,
        "present": 0,
        "absent": 0,
        "subjects": {}
    }

    print("Student added successfully.")

def add_subject():
    roll = input("Enter student roll number: ")

    if roll not in students:
        print("Student not found.")
        return

    subject = input("Enter subject name: ")

    if subject in students[roll]["subjects"]:
        print("Subject already exists.")
        return

    students[roll]["subjects"][subject] = {
        "present": 0,
        "absent": 0
    }

    print("Subject added successfully.")

def edit_student():
    roll = input("Enter roll number: ")

    if roll not in students:
        print("Student not found.")
        return

    print("Current name:", students[roll]["name"])

    new_name = input("Enter new student name: ")

    students[roll]["name"] = new_name

    print("Student details updated successfully.")
def delete_student():
    roll = input("Enter roll number: ")

    if roll not in students:
        print("Student not found.")
        return

    del students[roll]

    print("Student deleted successfully.")

def search_student():
    roll = input("Enter roll number: ")

    if roll not in students:
        print("Student not found.")
        return

    student = students[roll]

    print("\n===== STUDENT DETAILS =====")
    print("Roll Number:", roll)
    print("Student Name:", student["name"])
    print("Present:", student["present"])
    print("Absent:", student["absent"])

def dashboard():
    total_students = len(students)

    total_present = 0
    total_absent = 0

    for student in students.values():
        total_present += student["present"]
        total_absent += student["absent"]

    total_classes = total_present + total_absent

    if total_classes == 0:
        percentage = 0
    else:
        percentage = (total_present / total_classes) * 100

    print("\n===== ATTENDANCE DASHBOARD =====")
    print("Total Students:", total_students)
    print("Total Present:", total_present)
    print("Total Absent:", total_absent)
    print("Total Classes:", total_classes)
    print("Overall Attendance:", round(percentage, 2), "%")
def add_attendance_history():
    roll = input("Enter roll number: ")

    if roll not in students:
        print("Student not found.")
        return

    subject = input("Enter subject name: ")

    if subject not in students[roll]["subjects"]:
        print("Subject not found.")
        return

    date = input("Enter date (DD-MM-YYYY): ")

    status = input(
        "Enter P for Present or A for Absent: "
    ).upper()

    if status != "P" and status != "A":
        print("Invalid attendance choice.")
        return

    if "history" not in students[roll]:
        students[roll]["history"] = []

    students[roll]["history"].append({
        "date": date,
        "subject": subject,
        "status": status
    })

    print("Attendance history saved successfully.")

def show_history():
    roll = input("Enter roll number: ")

    if roll not in students:
        print("Student not found.")
        return

    if "history" not in students[roll]:
        print("No attendance history found.")
        return

    history = students[roll]["history"]

    if len(history) == 0:
        print("No attendance history found.")
        return

    print("\n===== ATTENDANCE HISTORY =====")

    for record in history:

        if record["status"] == "P":
            status = "Present"
        else:
            status = "Absent"

        print(
            "Date:", record["date"],
            "| Subject:", record["subject"],
            "| Status:", status
        )

def mark_subject_attendance():
    roll = input("Enter roll number: ")

    if roll not in students:
        print("Student not found.")
        return

    if len(students[roll]["subjects"]) == 0:
        print("No subjects found.")
        return

    print("\nSubjects:")

    for subject in students[roll]["subjects"]:
        print("-", subject)

    subject = input("Enter subject name: ")

    if subject not in students[roll]["subjects"]:
        print("Subject not found.")
        return

    choice = input(
        "Enter P for Present or A for Absent: "
    ).upper()

    if choice == "P":
        students[roll]["subjects"][subject]["present"] += 1
        print("Subject attendance marked Present.")

    elif choice == "A":
        students[roll]["subjects"][subject]["absent"] += 1
        print("Subject attendance marked Absent.")

    else:
        print("Invalid choice.")
def subject_report():
    roll = input("Enter roll number: ")

    if roll not in students:
        print("Student not found.")
        return

    print("\n===== SUBJECT ATTENDANCE =====")

    for subject, data in students[roll]["subjects"].items():

        present = data["present"]
        absent = data["absent"]
        total = present + absent

        if total == 0:
            percentage = 0
        else:
            percentage = (present / total) * 100

        print("\nSubject:", subject)
        print("Present:", present)
        print("Absent:", absent)
        print("Total Classes:", total)
        print(
            "Attendance:",
            round(percentage, 2),
            "%"
        )

        if percentage >= 75:
            print("Status: Eligible")
        else:
            print("Status: Shortage")

def show_students():
    print("\nStudent List")

    for roll, student in students.items():
        print(
            roll,
            student["name"],
            "Present:", student["present"],
            "Absent:", student["absent"]
        )


def mark_attendance():
    roll = input("Enter roll number: ")

    if roll not in students:
        print("Student not found.")
        return

    choice = input("Enter P for Present or A for Absent: ").upper()

    if choice == "P":
        students[roll]["present"] += 1
        print("Marked Present.")

    elif choice == "A":
        students[roll]["absent"] += 1
        print("Marked Absent.")

    else:
        print("Invalid choice.")
        
def show_attendance():
    roll = input("Enter roll number: ")

    if roll not in students:
        print("Student not found.")
        return

    student = students[roll]

    present = student["present"]
    absent = student["absent"]

    total = present + absent

    if total == 0:
        percentage = 0
    else:
        percentage = (present / total) * 100

    print("\n===== ATTENDANCE REPORT =====")
    print("Roll Number:", roll)
    print("Student Name:", student["name"])
    print("Total Classes:", total)
    print("Total Present:", present)
    print("Total Absent:", absent)
    print("Attendance Percentage:",
          round(percentage, 2), "%")

    if percentage >= 75:
        print("Status: Eligible")
    else:
        print("Status: Attendance Shortage")

def show_defaulters():
    print("\n===== STUDENTS BELOW 75% =====")

    found = False

    for roll, student in students.items():

        present = student["present"]
        absent = student["absent"]
        total = present + absent

        if total > 0:
            percentage = (present / total) * 100

            if percentage < 75:
                print(
                    "Roll:", roll,
                    "| Name:", student["name"],
                    "| Attendance:",
                    round(percentage, 2), "%"
                )

                found = True

    if found == False:
        print("No student has attendance below 75%.")
def class_statistics():
    total_students = len(students)

    total_present = 0
    total_absent = 0

    for student in students.values():
        total_present += student["present"]
        total_absent += student["absent"]

    total_classes = total_present + total_absent

    if total_classes == 0:
        percentage = 0
    else:
        percentage = (total_present / total_classes) * 100

    print("\n===== CLASS STATISTICS =====")
    print("Total Students:", total_students)
    print("Total Present:", total_present)
    print("Total Absent:", total_absent)
    print("Total Attendance Records:", total_classes)
    print(
        "Overall Attendance:",
        round(percentage, 2),
        "%"
    )
def main():

    while True:

        print("1. Add Student")
        print("2. Show Students")
        print("3. Mark Attendance")
        print("4. Show Attendance Report")
        print("5. Show Defaulters")
        print("6. Class Statistics")
        print("7. Add Subject")
        print("8. Mark Subject Attendance")
        print("9. Subject Report")
        print("10. Exit")
        print("11. Edit Student")
        print("12. Delete Student")
        print("13. Search Student")
        print("14. Dashboard")
        print("15. Add Attendance History")
        print("16. Show Attendance History")
        choice = input("Enter choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            show_students()

        elif choice == "3":
            mark_attendance()

        elif choice == "4":
            show_attendance()

        elif choice == "5":
            show_defaulters()

        elif choice == "6":
            class_statistics()

        elif choice == "7":
            add_subject()

        elif choice == "8":
            mark_subject_attendance()

        elif choice == "9":
            subject_report()

        elif choice == "10":
            print("Program ended.")
            break
        elif choice == "11":
            edit_student()
        elif choice == "12":
            delete_student()
        elif choice == "13":
            search_student()
        elif choice == "14":
            dashboard()
        elif choice == "15":
            add_attendance_history()

        elif choice == "16":
            show_history()

        else:
            print("Invalid choice.")
    
main()
