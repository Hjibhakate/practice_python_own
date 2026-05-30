students = []
attendances = {}

while True :

    print("\n === MINI ATTENDEANCE SYSTEM ====")

    print("1.Add Student ")
    print("2. Marks Attendance")
    print("3.Show Attendance ")
    print("4. Exist ")

    choice = input("Enter your choice: ")

    if choice == "1":

        name = input("Enter student name : ")

        students.append(name)

        print(name,"added successfully . ")

    elif choice == "2":
        if len(students)  == 0:
            print("No student found . ")
            continue
        print("\n Mark Attendance ")

        for student in students :
            status = input(f"{student} P/A : ").upper()

            if status == "P" :
                attendances[student] = "Absent"
            else:
                print("Invalid input.Marked as Absent. ")
                attendances[student] = "Absent"

    elif choice == "3":
        print("\n===Attendance List ===== ")

        if len(attendances)== 0 :
            print("No attendance recorded yet . ")
        else:
            for student,status in attendances.items():
                print(student,"-",status)

    elif choice == "4":
        print("program Ended . ")

        break 
    else:
        print("Invalid Choice. ")


        