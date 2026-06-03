students = []

while True :
    print("==================Student Marks Management System =================")
    print("1.Add Student")
    print("2. Show Srudent ")
    print("3 . Save to File ")
    print("4. Count Words ")
    print("5. Exist")


    choice = input("Enter Choice ")

    if choice == "1":
        name = input("Enter Student Name : ")
        math = int(input("Enter Math marks : "))
        science = int(input("Enter Science marks : "))

        student = {
            "name":name,
            "math":math,
            "science": science
            }

        students.append(student)
        print("Student Added ! ")


    elif choice == "2 ":
        print("\n Student Records : ")
        for student in students:
            print(student)

    elif choice == "3":
        with open("Students.txt","a") as file:
            for student in students :
                file.write(
                    f"Name:{student['name']}, Math: {student['math']}, Science: {student['science']}\n")

        print("Student data saved ")

    elif choice == "4":
        with open("students.txt","r") as file:
            content = file.read()

        words = content.split()
        print("Total words in file : ",len(words))

    elif choice == "5":
        print("Goodbye!")
        break 

    else:
        print("Invalid Choice " )