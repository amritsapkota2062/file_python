'''
EXCEPTION HANDALING
'''

# def divide_number():
#     try:
#         num1 = int(input("Enter your first number: "))
#         num2 = int(input("Enter your second number: "))

#         result = num1 / num2
#         print('result: ', result)

#     except ZeroDivisionError as e:
#         print(e)
#         print("You cannot divide a number by zero.")
#         divide_number()

#     except ValueError as e:
#         print('You must enter a valid number')


# try:
#     num1 = int(input("Enter your first number: "))
#     num2 = int(input("Enter your second number: "))
#     result = num1 / num2
#     print('result: ', result)
    
# except Exception as e:
#     print(e)
#     print("you have some issue on input")


'''
CUSTOM EXCEPTION
'''

# age = int(input("Enter your age: "))

# try:
#     if age < 0 or age > 120:
#         raise Exception("age must be between 0 and 120")
    
# except Exception as e:
#     print(e)

# multiple exception

# import traceback

# class AgeZeroError(Exception):
#     def __init__(self, message):
#         self.message = message

#         super().__init__(self.message)


# class HighestError(Exception):
#     def __init__(self, message):
#         self.message = message

#         super().__init__(self.message)

# try:
#     age = int(input("Enter your age: "))

#     if age < 0:
#         raise AgeZeroError("age is zero.")

#     elif age > 120:
#         raise HighestError("Age is greater than 120.")
    
# except AgeZeroError as e:
#     traceback.print_exc()
#     print(e)

# except HighestError as e:
#     print(e)

# value = input("Enter something")
# try:

#     if value.isdigit():
#         value = int(value)
#         print(value)
#     elif "." in value:
#         value = float(value)
#         print(value)

# except Exception as e:
#     print(e)
#     print("You have to input only one .")

'''
1. Student Class

Create a class Student with:

attributes: name, age, marks
method to display student details
method to check if student passed (marks >= 40)
2. Rectangle Class

Create a class Rectangle with:

length and breadth
method to calculate area
method to calculate perimeter
3. Bank Account

Create a class BankAccount with:

account holder name
balance

Methods:

deposit money
withdraw money
display balance

Also prevent withdrawing more than available balance.

4. Car Class with Constructor

Create a class Car using __init__().

Attributes:

brand
model
price

Method:

display all car information
5. Inheritance Practice

Create:

a parent class Animal
child classes Dog and Cat

Each should have a method:
'''

# # 
# Create a class Student with:

# attributes: name, age, marks
# method to display student details
# method to check if student passed (marks >= 40)

# class Student:
#     def __init__(self, name, age, marks):
#         self.name = name
#         self.age = age
#         self.marks = marks

#     def display(self):
#         print(f"The student name is {self.name}, who is {self.age} years old. His marks is {self.marks}.")

#     def did_pass(self):
#         if self.marks >= 40:
#             print("The student passed the examination.")

#         else:
#             print("The student failed the examination.")

# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# marks = float(input("Enter your marks: "))

# std = Student(name, age, marks)
# std.display()
# std.did_pass()


# Create a class Rectangle with:

# length and breadth
# method to calculate area
# method to calculate perimeter

# class Rectangle:
#     def __init__(self, length, breadth):
#         self.length = length
#         self.breadth = breadth

#     def area(self):
#         return f"Area of {self.length} and {self.breadth} is {self.length * self.breadth}"
    
#     def perimeter(self):
#         return f"Perimeter of {self.length} and {self.breadth} is {2*(self.length + self.breadth)}"
    

# length = float(input("Enter the length: "))
# breadth = float(input("Enter a breadth : "))

# rect = Rectangle(length, breadth)

# print(rect.area())
# print(rect.perimeter())


# Create a class BankAccount with:

# account holder name
# balance

# Methods:

# deposit money
# withdraw money
# display balance

# Also prevent withdrawing more than available balance.

# class BankAccount:
#     def __init__(self, ac_holder_name, balance):
#         self.name = ac_holder_name
#         self.balance = balance

#     total_balance = 0


#     def deposit(self):
#         amount = float(input("Enter how much you want to deposit: "))
#         self.total_balance += amount

#     def withdraw(self):
#         amount = float(input("Enter the amount you want to withdraw: "))

#         if amount <= self.balance:
#             print(f"Here is your withdrawl balance: {amount}")
#             self.total_balance -= amount

#         else:
#             print(f"You dont have sufficient amount in your bank account.")

#     def display(self):
#         print(f'Your total balance is {self.total_balance}.')

# name = input("What is your name? ")
# balance = float(input("Enter your bank balance:  "))
# print(f"Hello {name}!")

# while True:
#     continue_activity = input("Do you want to continue activity? Y or N ? ")

#     if continue_activity.lower() == 'y':
    
#         task = int(input("What do you want to do?\n1)Deposit\n2)Withdraw\n3)Display? "))

#         acc_holder = BankAccount(name, balance)

#         if task == 1:
#             acc_holder.deposit()

#         elif task == 2:
#             acc_holder.withdraw()

#         elif task == 3:
#             acc_holder.display()

#         else:
#             print("Enter a valid task.")

#     else:
#         break

# num1 = int(input("Enter number 1: "))
# num2 = int(input("Enter number 2: "))

# try:
#     divide = num1 / num2
#     print(divide)

# except ZeroDivisionError as e:
#     print(e)
#     print("The number cannot be divided by zero.")


# try:
#     number = int(input("Enter numbers : "))
#     print(number)

# except ValueError as e:
#     print(e)
#     print("Enter only numbers.")





