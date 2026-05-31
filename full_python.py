def print_table(number):

    for i in range (1,11):
        print( number," * ", i ,"=" , number * i ) 

num = int(input("Enter the number you want to print : "))

print_table(num)