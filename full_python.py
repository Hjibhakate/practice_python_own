expense = []

def add_expense():
    amount = float( input("Enter expense amount :  "))
    expense.append(amount)
    print("Expense added successfully . ")


def show_expenses():
    if len(expense) == 0 :
        print("No expenses found ")
    else:
        print("\n Expense : ")
        for i , amount in enumerate(expense, start = 1):
            print(f"{i}. rs{amount}")

def total_spending():
    print("Total Spending = rs ", sum(expense))


def highest_expense():
    if len(expense) ==  0 :
        print ("No expenses found. ")
    else:
        print("Highest Expense = Rs ", max(expense))

while True :
     print("===== EXPENSE TRACKER ====== ")
     print("1. Add Expenses ")
     print("2. Show Expenses ")
     print("3. Total Spending ")
     print("4. Highest Expense ")
     print ("Exit ")


     choice = input('Enter your choice : ')


     if choice == "1":
         add_expense()
     elif choice == "2":
         show_expenses()
     elif choice == "3":
         total_spending()
     elif choice == "4":
         highest_expense()
     elif choice == "5":
         print("Program Ended . ")
         break 
     else :
          print("Invalid  Choice ")