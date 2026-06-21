class Student:
    def __init__(self,name, marks):
        self.name = name
        self.marks = marks 

    def display(self):
        print(f"my name is {self.name} and {self.marks}")

    def new(self,extra):
        self.marks += extra
        print(f"my  extra marks is {self.marks}")

p1 = Student("harshad",99)

p1.display()
p1.new(10)
p1.display()