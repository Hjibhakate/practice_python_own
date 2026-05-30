import math 

def rectangle():

    length = float(input("Enter length : "))

    breadth = float(input("Enter breadth :"))

    return length * breadth

def circle():

    radius = float(input("Enter the radius : "))

    area = math.pi*radius*radius

    circumference = 2*math.pi*radius

    print("Area of Circumference of circle = ",round(circumference,2))

    return area 

def triangel():

    base = float(input("enter the bases : "))

    height = float(input("Enter the hight : "))

    return 0.5*base*height

while True :

    print("=======Area Calculater ======")

    print("1.Rectangel")
    print("2.Circle")
    print("3.Triangel")
    print("4.Exist ")


    choice = input("Enter  your choice : ")

    if choice == "1":
        area = rectangle()

        print("Area of Rectangel= ",area )

    elif choice =="2":
        area = circle()

        print("Area of Circle= ",round(area,2))

    elif choice == "3":
        area = triangel()

        print("Area of triangel is = ",area )

    elif choice == "4":
        print("program Ended ")
        break 
    else:
        print("Invalid Choice ")

    #kjnkj