students = {}

def calcualte_grade(marks):

    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "Fail"

def add_student():

    name = input("Enter the Student name : ")

    marks = float(input("Enter marks : "))

    students[name] = marks 

    print("Student added successfully . ")


def delete_student():

    name = input("Enter student name to delete : ")

    if name in students:

        del students[name]

        print("Student deleted successfully. ")
    else:
        print("Student not found . ")

def search_student():

    name = input("Enter student name to search : ")

    if name in students :

        marks = students[name]

        grade = calcualte_grade(marks)

        print("\n Student Founs ")

        print("Name : ",name)
        print("Marks: ",marks)
        print("Grade: ",grade)
    else:
        print("Student not found . ")

def show_students():

    if len(students) == 0 :
        print("No student available ")

    else:
        print("\n === STUDENT LIST ===== ")

        for name ,marks  in students.items():

            grade = calcualte_grade(marks)

            print(f"Name : {name } | Marks : {marks} | Grade : {grade}")

while True :

    print("\n === STUDENT MANAGEMENT SYSTEM ========== ")

    print("1. Add Student ")
    print('2. Delete Student ')
    print("3. Search Student ")
    print(" 4. Show All Students ")
    print("5. Exit ")


    choice = input("Enter you choice : ")

    if choice == "1":
        add_student()
    elif choice == "2":
        delete_student()
    elif choice == "3":
        search_student()
    elif choice == "4":
        show_students()
    elif choice == "5":
        print("program ended . ")
        break 
    else :
        print("Invalid Choice! ")