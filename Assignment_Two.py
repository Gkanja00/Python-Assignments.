#QUESTIONS
#1 The volume of a sphere with radius r is (4/3)* pie * r**2.
#What is the volume of the sphere with radius 5.
#Make sure the program enters the radius from the keyboard and provide the answer in 2 deciml places



radius = int(input("Enter the radius of the sphere: "))
volume = (4/3) * (22/7) * radius**2
print(f"The volume of the sphere with radius{radius} is: {volume:.2f}")
   

 # Create a program to calculate the area of a triangle (1/2 * base * height). 
# Base and height should be entered using the keyboard. 

base = int(input("Enter the base of the triangle: "))
height = int(input("Enter the height of the triangle: "))
area = (1/2 * base * height)                       
print(f"The area of the triangle with base {base} and height {height} is: {area}")

# WITI has tasked you to automate a simple grading system. 
# As a python student, write a program using to display the grades that 
# the students will be receiving based on the mark scored in a subject. 
# The grades are:
# 90% - 100% Grade is A
# 80% - 89% Grade is B
# 70% - 79% Grade is C                                                        
# 60% - 69% Grade is D                  
# 50% - 59% Grade is E  
# < 50% Fail 

def calculate_grades():
   print("\n...Student Grade Calculations...")
   mark = int(input("Enter mark scored:\t"))
  
   if mark>= 90  and mark <=100:
      print(' Grade is A')

   elif mark>=80 and mark <= 89:
         print('Grade is B')

   elif  mark >=70 and mark<=79:
         print('Grade is C')

   elif  mark >=60 and mark<=69:
         print('Grade is D')

   elif  mark >=50 and mark<=59:
        print('Grade is E')

   else:
         print('Fail')
    
# calculate_grades()


 #WITI Academy is proposing a Sacco to help students save their money. 
# Design a platform that will do the following.
# Welcome to, WITIAcademy Sacco.
# 1. Deposit Money
# 2. Withdraw Money
# 3. Check Balance
# Ensure if the student selects 1, money is deposited and the minimum deposit should be 1000.
# If the student selects 2, money should be withdrawn and a minimum withdrawal is 500.
# If the student selects 3, the account balance should be displayed.

def sacco_transactions():
    account_balance = 0
    run = 1
    while run == 1:
        print("\nWelcome to, WITIAcademy Sacco.")
        print('1. Deposit Money')
        print('2. Withdraw Money')
        print('3. Check Balance')
        studentchoice = int(input("Enter your selection(1,2, or 3): "))
        if studentchoice == 1:
            print("\n...Processing a deposit transaction...")
            depositamount = int(input("Enter amount to be deposited): "))
            if depositamount <1000:
                print("\nMinimum deposit is 1000")
        else:
            accountbalance=+ depositamount
            print(f"Dear student, you have deposited {depositamount:,} and your new account balance is{account_balance:,}")
        
        if studentchoice == 2:
            print("\n...Processing a withdraw transaction...")
        withdrawamount = int(input("Enter amount to be withdrawn): "))
        if account_balance ==0:
            print("Your account balance is 0")
        elif withdrawamount < 500:
            print("Minimum withdraw amount is 500")
        if withdrawamount > account_balance:
            print("withdraw failed, insufficient funds")
        else:
            account_balance= account_balance - withdrawamount
            print(f"Dear student, you have withdrawn {withdrawamount:,} and your new account balance is{account_balance:,}")


        if studentchoice == 3:
            print(f"Your account balance is {account_balance:,}")
    
        else:
            print("You entered a wrong choice!! Please select 1, 2, or 3\n")
        
        run = int(input("Enter 1 to continue or any number to exit: "))
        if run!=1:
            print('Thanks for using our Sacco')
            break
sacco_transactions()
    

             
             
             
               
