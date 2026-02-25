# #Exercise 1: Check a number is even or odd
# num = int(input("Enter a number : "))
# if num % 2 == 0:
#     print("Even number")
# else:
#     print("Odd number")

# #Exercise 1 : Check for a leap year 

# year = int(input("Enter a year : "))
# if (year % 400 == 0 ) or (year % 4 == 0 and year % 100 != 0 ):
#     print("Leap year ")
# else:
#     print("Not a leap year ")

# #Exercise 1:cHECK IF A NUMBER IS POSITIVE , NEGATIVE OR ZERO .
# num = int(input("Enter a number is : "))
# if num > 0:
#     print("Positive")
# elif num < 0:
#     print("Negative")
# else:
#     print("Zero")

# #Exercise 1 : Check for the Greater than 100 or not 
# num = int(input("Enter a number : "))
# if num > 100:
#     print("Greater than 100")
# else:
#     print("The number is 100 or less than 100")


# #Exercise 1 :Check for the Divisible by 5

# num = int(input("Enter a number : "))
# if num % 5 == 0:
#     print("The Number is Divisible by 5 ")
# else:
#     print("The number is not Divisible by 5 ")

# #Exercise 1 :Find largest of two Number 
# a = int(input("Enter First Number : "))
# b = int(input("Enter second Number : "))

# if a > b:
#     print("First number is greater ")
# elif b > a:
#     print("Second number is greater ")
# else:
#     print("Both are equal ")

# #Exercise 1 :Find Largest of three Numbers

# a = int(input("Enter first number : "))
# b = int(input("Enter Second number : "))
# c = int(input("Enter a Third number : "))

# if a >= b and a >= c :
#     print("First number is largest ")
# elif b >= a and b >=c:
#     print("Second number is largest ")
# else:
#     print("Third number is largest ")

# #Exercise 1 : Check for voting eligibility 
# age = int(input("Enter your age : "))
# if age >= 18 :
#     print("Eligible to vote ")
# else:
#     print("Not eligible to vote ")

# #Exercise 1 : Grade Based on Marks

# marks = int(input("Enter Marks : "))

# if marks >= 90:
#     print("Grade A")
# elif marks >= 75:
#     print("Grade B")
# elif marks >= 50 :
#     print("Grade C")
# else:
#     print("Fail")

# #Exercise 1 :Simple Calculator
# a = int(input("Enter first number : "))
# b = int(input("Enter second number : "))
# op = input("Enter operator (+,-,*,/): ")

# if op =="+":
#     print(a+b)
# elif op =="-":
#     print(a-b)
# elif op =="*":
#     print(a*b)
# elif op =="/":
#     print(a/b)
# else:
#     print("Invalid operator ")

# #Exercise 1 : Print number 1 to 20
# for i in range(1,20):
#     print(i)

# #Exercise 1 : Print number from 10 to 1
# for i in range(10,0,-1):
#     print(i)

# # Exercise 1: print even number from 1 to 20
# for i in range(1,21):
#     if i % 2 == 0:
#         print(i)

# #Exercise 1 :Print odd number from 1 to 20 
# for i in range(1,21):
#     if i % 2 != 0:
#         print(i)

# #Exercise 1 : print square of numbers 
# for i in range(1,11):
#     print(i,"Square is ",i*i)

# #Exercise 1: Sum of numbers from 1 to 10 
# total = 0
# for i in range(1,11):
#     total += i
#     print("Sum = ",total)


# #Exercise 1 :Multipication table of 5 
# for i in range(1,11):
#     print("5 * ",i,"=",5*i)

#Exercise 1: Print all the items in list 
# numbers = [2,4,6,8,10 ]
# for i in numbers:
#     print(i)

#Exercise 1 :Count number greater than 10 

# nums = [5,12,18,7,3,20]
# count = 0
# for i in nums:
#     if i > 10:
#         count += 1
#         print("Count = ", count )


# #Exercise 1 :print stars
# for i in range(5):
#     print("*")

# #Exercise 1 :star pattern 
# for i in range(1,6):
#     print("*"*i)

# #Exercise 1: Function to add two number
# def add(a,b):
#     return a+b
# print(add(2,5))

# #Exercise 1 :Function to sub two number 
# def sub(a,b):
#     return a-b
# print(sub(9,7))

# #Exercise 1 :Function to mul two number
# def mul(a,b):
#     return a*b
# print(mul(1,2))

# #Exercise 1 :Function to div two numbers
# def  div(a,b):
#     return a/b
# print(int(div(9,3)))

# #Exercise 2 :Function to div two numbers
# def div(a,b):
#     return a/b
# print(div(3,4))

# #Exercise 1 :Work with a list 
# fruits = [ "apple ", "banana","mango"]
# fruits.append("orange")
# for fruit in fruits:
#     print(fruit)

# exercise 1 : for the dictionaries 
# student = {"name":"harshu","math":99 , "science":99 }
# print(student["name"],"got",student["math"],"in math ")



#Exercise 1: write and read a file 
# with open("example.txt","w") as f:
#     f.write("Hello Python \nLearning is fun!")

# with open("example.txt","r") as f:
#     content = f.read()
#     print(content)





# Example 1 : Append more lines, count number of words in the file .

#File name
file_name = "sample.txt"

#  1 Append more lines to the file 
with open(file_name,"a") as file:
    file.write("\nThis is an appended line . ")
    file.write("\nPython makes file handling easy.")

print("Lines appended successfully.")

# 2. Count number of words in the file 
with open(file_name,"r") as file :
    content = file.read()
    words = content.split()
    word_count =len(words)


print("Total number of words in the file: ", word_count )


#Exercise 2 . Append more lines,count number of words in the file .
#file name 
file_name = "sample.txt"

#1 Append more lines to the  file 
with open(file_name,"a")as file:
    file.write("\n This is an appended Line. ")
    file.write("\nPython makes file handling easy .")

print("Lines append successfully. ")

# 2 .Count number of words in the file  
with open(file_name,"r")as  file:
    content= file.read()
    words = content.split()
    word_count = len(words)

print("Total numver of words in the file : ",word_count)


#Exemple 3 :Append more lines,count number of words in the file 

#File name 
file_name = "sample.txt"

#1 append more line to the file 
with open(file_name,"w")as file:
    file.write("\n This is an append lines. ")
    file.write("\n Paython makes file handling easy . ")

print("Lines append successfully . ")

#2   count the number of words in the file 

with open(file_name,"r")as file:
    content = file.read()
    words = content.split()
    word_count = len(words)

print("Total number of words in the file: ", word_count)



#Exercise 4 :Append more lines , count number of words in the file 

#file name 
file_name = "sample.txt"

#1 append more lines to the file 
with open(file_name,"w") as f:
    f.write("\n This is an appended line ")
    f.write("\n Python makes file handling easy. ")

print("Lines appended successfully . ")


#2 count number of words in the file 
with open(file_name,"r" ) as f:
    content = f.read()
    words = content.split()
    word_count = len(words)

print("Total number of words in the file: ",word_count) 


#Exercise 5 : Append more lines , count number of words in the file 

#File name 
file_name = "sample.txt"

#1 . Append more lines to the file 
with open(file_name,"w" )as f :
    f.write("\n This is an appended line")
    f.write("\n Python makes file handling easy . ")

print("Lines appended successfully ")


#2. Count number of words in the file 
with open(file_name,"r") as f :
    content = f.read()
    words = content.split()
    word_count = len(words)


#Exercise 6 Append more lines , count number of words in the file 
#File name 
file_name = "sample.txt "

#1. aPPEND MORE LINES TO THE file 
with open(file_name,"w" )as f :
    f.write("\n This is an appended lines. ")
    f.write("\n Python makes file handling easy . ")

print("Lines append successfully ")


#2 Count number of words in the file 
with open(file_name,"r") as f:
    content = f.read()
    words = content.split()
    word_count = len(words)

print("Total number of words in the file : ",word_count)


#Exercise 7 :Append more lines ,Count number of words in the file 
#File name 
file_name = "sample.txt"

#Append more lines 
with open(file_name,"w") as f :
    f.write("\nThis is an appended line. ")
    f.write("\nPython makes file handling easy. ")

print("Lines appended successfully ")


#Count number of words in the file 
with open(file_name,"r") as f:
    content = f.read()
    words = content.split()
    word_count = len(words)

print("Total number of words in the file






