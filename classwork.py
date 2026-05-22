# Question1

# number = [1, 2, 3, 4, 5, 6, 7, 8]
# # new_number = ["e" if x % 2 == 0 else x for x in number]
# # print(new_number)

# "Question2"

# # fruits = ["apple", "banana", "ggg", "hhh", "fff"]
# # new_fruits = ["vowel" if "a" in x.lower() or "e" in x.lower() or "i" in x.lower() or "o" in x.lower() or "u" in x.lower() else "non-vowel" for x in fruits]

# # print(new_fruits)
# # "Question 3"
# number = [1, 2, 3, 4, 5]
# # new_number = [4, 2, 6, 4, 8]

# new_number = [x+3 if x % 2 != 0 else x for x in number]

# print(new_number)
# # #Question 4
# # fruits = ["APPLE", "cherry", "BANANA", "orange", "PINE"]
# # new_fruits = [x.lower() if x.isupper() else x.upper() for x in fruits]
# # print(new_fruits)

'''
Take numbers from 1 to 50 and:

Find the sum of all numbers divisible by 3
Find the sum of all numbers divisible by 5
Print both separately.
'''
# sum1 = 0
# sum2 = 0

# for i in range(1, 51):
#     if i % 3 == 0:
#         sum1 += i
#     if i % 5 == 0:
#         sum2 += i

# print(f"Sum of numbers divisible by 3 = {sum1}\nSum of numbers divisible by 5 = {sum2}")


'''
Ask the user for a number n.
Print all prime numbers from 1 to n.
'''

# n = int(input("Enter a number upto which prime numbers can be printed: "))
# prime_numbers = []

# for num in range(1, n+1):
#     no_of_divisibles = 0

#     for i in range(1, num+1):
#         if num % i == 0:
#             no_of_divisibles += 1

#     if no_of_divisibles == 2:
#             prime_numbers.append(num)

# print(prime_numbers)

'''
Take a string input from the user and:

Reverse it using a loop (NOT [::-1])
Check if it is a palindrome
'''

# user_input = input("Enter a string to reverse it: ")
# reversed_string = ""
# for s in range(len(user_input)-1, -1, -1):
#     reversed_string += user_input[s]

# if user_input == reversed_string:
#     print(f"The letter {reversed_string} is a palindrome.")

# else:
#     print(f"The letter {user_input} is not palindrome.")

'''
Print its multiplication table up to 10
Skip multiples of 5 using continue
'''

# n = int(input("Enter a number to find it's multiple: "))

# for i in range(1, 11):
#     if i == 5:
#         continue
    
#     print(f"{n} * {i} = {n*i}")



'''
Sets and tuples questions
'''

# Question1

'''
create me the bingo jgame using set
when user enter "y" it should pick me number
'''
# num_set = set()
# for i in range(1, 100):
#     num_set.add(i)

# # should_stop = True
# # while should_stop:
# #     should_pick = input("Do you want to pick a number?\nY/N? ")
# #     if should_pick == 'n':
# #         break
# #     if should_pick.lower() == 'y':
# #         print(num_set.pop())
# #     if len(num_set) == 0:
# #         print(f"You have picked all the numbers.")
# #         break
# # Question2

# '''
# generate 4-digit otp number from range of onumbers store in set
# '''

# otp = set()

# for i in range(4):
#     otp.add(str(num_set.pop()))

# print(otp)



# student = {
#     "name": "ram",
#     "roll" : 12,
#     "address": "ktm",
#     "phone_number": [987654321, 9087655443],
#     "marks": [70, 50, 60, 40, 40],
#     "age": 20
# }

# student["total_marks"] = sum(student["marks"])

# student = {}

# name = input("Enter your name: ")
# student['name'] = name

# roll = int(input("Enter your roll number: "))
# student['roll'] = roll

# address = input("Enter your address: ")
# student['address'] = address

# age = int(input("Enter your age: "))
# student['age'] = age

# phone_number = []
# no_of_numbers = int(input("How many numbers do you have? "))

# while no_of_numbers != 0:
#     num = input("Enter your numbers: ")

#     if len(num) == 10 and num.isdigit():
#             phone_number.append(int(num))
#             no_of_numbers -= 1

#     else:
#           print("Your number should be equal to 10.")
# student['phone_number'] = phone_number

# marks = []
# no_of_sub = int(input("How many subjects marks? "))

# while no_of_sub != 0:
#       mark = int(input("Enter your marks: "))

#       if mark > 0 and mark <= 100:
#             marks.append(mark)
#             no_of_sub -= 1

#       else:
#             print("Enter a valid mark.")
# student["marks"] = marks

# print(student)



# student = {
#     "name": "ram",
#     "roll": 12, 
#     "address": "ktm",
#     "contact": {
#         "email": "ram.123@gmail.com",
#         "phone number": [1234567890, 9087654321]
#     },
#     "subject": {
#         "math": 20,
#         "science": 50,
#         "computer": 60
#     }
# }

# student = {}

# subject = {}
# subject["math"] = int(input("Enter you mark in mathematics: "))
# subject["science"] = int(input("Enter you mark in science: "))
# subject["computer"] = int(input("Enter your mark in computer: "))
# student["subject"] = subject

# contact = {}
# contact["email"] = input("Enter your email address: ")
# no_of_num = int(input("How many numbers do you have? "))
# numbers = []

# while no_of_num != 0:
#     number = input("Enter your number: ")
#     if len(number) == 10 and number.isdigit():
#         numbers.append(number)
#         no_of_num -= 1

#     else:
#         print("please enter a valid number.")
# contact["phone number"] = numbers
# student["contact"] = contact

# student["name"] = input("Enter your name: ")
# student["roll"] = int(input("Enter your roll no: "))
# student["address"] = input("Enter your address: ")
# print(student)


# students = {}

# no_of_std = int(input("How many students are there? "))

# while no_of_std != 0:
#     student = {}

#     roll_no = int(input("Enter your roll number: "))

#     subject = {}
#     subject["math"] = int(input("Enter you mark in mathematics: "))
#     subject["science"] = int(input("Enter you mark in science: "))
#     subject["computer"] = int(input("Enter your mark in computer: "))
#     student["subject"] = subject

#     contact = {}
#     contact["email"] = input("Enter your email address: ")
#     no_of_num = int(input("How many numbers do you have? "))
#     numbers = []

#     while no_of_num != 0:
#         number = input("Enter your number: ")
#         if len(number) == 10 and number.isdigit():
#             numbers.append(number)
#             no_of_num -= 1

#         else:
#             print("please enter a valid number.")
#     contact["phone number"] = numbers
#     student["contact"] = contact

#     student["name"] = input("Enter your name: ")
#     student["address"] = input("Enter your address: ")
#     students[f"student_{roll_no}"] = student
#     no_of_std -= 1

# for key, value in students.items():
#     print(f"{key} : {value}\n")


'''
FUNCTIONS CLASSWORK
'''

# def task():
#     operation = int(input(("What do you want to do?\n1) addittion\n2) subtraction\n3) multiplication\n4) division\n")))
#     return operation

# def addition(num1, num2):
#     return num1 + num2

# def subtraction(num1, num2):
#     return num1 - num2

# def multiplication(num1, num2):
#     return num1 * num2

# def division(num1, num2):
#     return num1 / num2

# while True:
#     continue_task = input("Do you want to do something? Y/N: ")
#     if continue_task.lower() == 'n':
#         print("Thankyou for playing!")
#         break

#     else:
#         task = task()

#         num1 = int(input("Enter the first number: "))
#         num2 = int(input("Enter the second number: "))
#         if task == 1:
#             print(f"num1 + num2 = {addition(num1, num2)}")

#         elif task == 2:
#             print(f"{num1} - {num2} = {subtraction(num1, num2)}")

#         elif task == 3:
#             print(f"{num1} * {num2} = {multiplication(num1, num2)}")

#         elif task == 4:
#             print(f"{num1} / {num2} = {division(num1, num2)}")

#         else:
#             print("Enter a valid task.")

# def calculator(x, y):
#     add = x + y
#     sub = x - y
#     mul = x * y
#     div = x / y
#     # return {"addition": add, "subtraction": sub, mul, div}
#     return [add, sub, mul, div]

# x = int(input("Enter num1: "))
# y = int(input("Enter num2: "))

# final_result = calculator(x, y)

# # add, sub, mul, div = final_result
# # print(f"Addition = {add}")

# def value(x):
#     return max(x), min(x), sum(x)

# numbers = [1, 2, 3, 4, 5]
# max_value, min_value, sum_value = value(numbers)
# print(f"You max value is {max_value}")
# print(f"Your min value is {min_value}")
# print(f"Sum is {sum_value}")


# def reverse_string(s):
#     if s == "":
#         return ""
#     return reverse_string(s[1:]) + s[0]


# user_input = input("Enter a string: ")

# reversed_word = reverse_string(user_input)

# print("Reversed string:", reversed_word)

class addition:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def returning(self):
        return f"{self.num1} + {self.num2} = {self.num1 + self.num2}"
    
class subtraction:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def returning(self):
        return f"{self.num1} - {self.num2} = {self.num1 - self.num2}"
    
class multiplication:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def returning(self):
        return f"{self.num1} * {self.num2} = {self.num1 * self.num2}"
    
class division:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def returning(self):
        return f"{self.num1} / {self.num2} = {self.num1 / self.num2}"
    
task = input("What do you want to do? (+, -, *, /): ")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if task == '+':
    add = addition(num1, num2)
    print(add.returning())

elif task == '-':
    sub = subtraction(num1, num2)
    print(sub.returning())

elif task == '*':
    mul = multiplication(num1, num2)
    print(mul.returning())

elif task == "/":
    div = division(num1, num2)
    print(div.returning())