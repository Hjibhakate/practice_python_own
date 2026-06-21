class Person :
    def __init__(self,name ,age):
        self.name = name 
        self.age = age 
    def greet(self):
        print(f"my name is {self.name} and my age is {self.age}")

    def new_age(self):
        self.age += 1
        print(f"my new age is {self.age}")

    def new_name(self,change_name):
        self.change_name = change_name
        print(f"my new change name is {self.change_name}")

p1 = Person("harshad",22)
p1.greet()
p1.new_age()
p1.new_name("hemu")