# i = 0
# sum = 0
# while i < 10:
#     print(i)
#     sum += i
#     i += 1

# print(sum)

# sum_odd = 0
# sum_even = 0
# i = 0

# while i < 10:
#     if i % 2 == 0:
#         sum_even += i
    
#     else:
#         sum_odd += i
#     i += 1
# print(sum_even) 
# print(sum_odd)

# sum = 0

# while True:
#     n = int(input("Enter a number: "))
#     if n == 0:
#         break
    
#     elif n == 5:
#         continue
#     sum += n 

# print(f"Sum: {sum}")

# '''
# question: take user input any number and check if the number is prime or not
# '''
# no_of_divisibles = 0
# num = int(input("Enter a number to check whether the number is prime or not: "))

# for i in range(1, num):
#     if num % i == 0:
#         no_of_divisibles += 1

# if num == 1 or num == 0:
#     print(f"It is not prime numbers")

# else:
#     if no_of_divisibles > 1:
#         print(f"the number {num} is not a prime number.")

#     elif no_of_divisibles <= 1:
#         print(f"The number {num} is a prime number.


# s = ("Hello World!")

# # for i in range(len(s)):
# #     print(s[i], i)
# ind = 0
# for x in s:
#     print(x, ind)
#     ind += 1

# word = input("Enter a word to check whether the word is palindrome or not: ")
# new_word = word[::-1]

# # for i in range(1, len(word) + 1):
# #     new_word += word[-i]

# if word == new_word:
#     print("The word is palindrome.")
# else:
#     print("The word is not palindrome.")


# #Another logic

# s = "Hello"

# s = "h" + s[1:] + " python"
# print(s)


# word = "Hello Python!"
# new_word = ""

# for i in range(len(word), 0, -1):
#     new_word += word[i-1]

# print(new_word)

# s = "Hello World!"
# print(s.replace('World', 'Python'))
# print(s)

# s = "  ####Hello #### World! ######   ".strip()
# # print(s.lstrip())
# # print(s.rstrip())
# # print(s.strip())
# print(s.lstrip("#"))
# print(s.rstrip("#"))
# print(s.strip("#"))


# s = "aaaaabbbbbdddddccccccHello Pythond!dddddddbbbbbaaaaacccc"
# print(s.strip("abcd"))

# s = "Hello$World!"

# print(s.split("$"))

# lis = ["Hello", "World", "Python"]

# # s = "  #".join(lis)
# # print(s)
# s = " ".join(lis)
# print(s)

# num = "12345aaaabb"
# print(num.isdigit())


# input_string = "#@!@#%$Hello#$#world$#@!@%".strip("!@#$%")

# value1 = input_string.strip("!@#$%")

# value2 = value1[:5] + " " + value1[8:]

# print(value2)
# # vowels = ['a', 'e', 'i', 'o', 'u']
# # count = 0
# # s = input("Enter something: ").lower()

# # for i in s:
# #     if i in vowels:
#         count += 1

# print(f"There are {count} vowels in your sentence.")


'''
List in python
'''

# numbers = [1, 2, 3, 4, 5]

# print(numbers)
# numbers.insert(2, 100)

# print(numbers)

# # remove the items containing a
# fruits = ["apple", "banana", "cherry", "pine", "orAnge"]
# filtered_fruits = []
# print(fruits)
# for i in fruits:
#     if 'a' not in i.lower():
#         filtered_fruits.append(i)
# print(filtered_fruits)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# #scan all the above numbers and update all even numbers in above list with EVEN
# for i in range(len(numbers)):
#     if numbers[i] % 2 == 0:
#         numbers[i] = "EVEN"

# print(numbers)

# numbers = [1, 1, 1, 2, 3, 4, 5, 3]
# new_list = []

# for i in numbers:
#     if i not in new_list:
#         new_list.append(i)

# print(new_list)

# fruits = ["apple", "banana", "cherry", "ggg", "fff", "hhh"]
# vowels = "aeiou"
# new_fruits = list(fruits)

# for i in fruits:
#     has_vowel = False
#     for v in i:
#         if v in vowels:
#             has_vowel = True
#             break
#     if not has_vowel:
#         new_fruits.remove(i)

# print(new_fruits)




# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# # sum = 0
# # for values in matrix:
# #     for i in values:
# #         sum += i 

# # print(sum)
# multiple = 1
# # for i in range(len(matrix)):
# #     multiple *= matrix[i][i]

# for i in range(len(matrix)):
#     print(matrix[i])
#     multiple *= matrix[i][-i]
# print(multiple)


# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# multiple = 1
# # num = 0
# # for i in range(len(matrix),0, -1):
# #         multiple *= matrix[i-1][num]
# #         num += 1

# c = len(matrix)

# for r in range(c):
#     multiple *= matrix[r][c-1-r] 
# print(multiple)

  



# Sort

# number = [4, 6, 3, 6, 3, 7, 3]
# # number.sort()
# # number.sort(reverse= True)
# # print(number)

# '''
# sort strings
# '''
# # fruits = ["pine", "orange", "apple", "banana", "app", "Zoo"]
# # fruits.sort()
# # print(fruits)
# # fruits.sort(reverse=True)
# # print(fruits)

# #sorted
# new_number = sorted(number)
# print(new_number)
# print(number)

# # Copy
# number = [1, 2, 3, 4, 5]

'''
Methods of copying list 
'''
# 1) new_number = number.copy()
# 2) new_number = list(number)
# 3) new_number = number[:]


# print("number: ", number)
# print("new_number: ", new_number)
# number.append(100)

# print("number: ", number)
# print("new_number: ", new_number)

# extend()
# num1 = [1, 2, 3, 4, 5]
# num2 = [6, 7, 8, 9]

# num1.extend(num2)
# print(num1)


# list comprehension -> approach for if
# fruits = ["apple", "banana", "cherry"]
# new_fruits = [x for x in fruits if "a" in x]
# print(new_fruits)

# list comprehension -> approach for if and else
# number = [1, 2, 3, 4, 5, 6, 7, 8]
# new_number = ["e" if x % 2 == 0 else "o" for x in number]
# print(new_number)

# list comprehension -> approach of for only

# number = [1, 2, 3, 4, 5, 6, 7, 8]
# new_number = [x ** 2 for x in number]
# print(new_number)

'''
Tuple unpacking
'''

# num1, num2, *num3 = (1, 2, 3)


# Sets
#x.add("abc")

# Delete
# set.remove("abc") -> It remove the item but if the item is not there it produces error

# set.discard("aaa") -> It removes and doesn't create error

# fruits = {"abc", "xyz"}
# # fruits.remove("aaa")
# # fruits.discard("aaa")
# print(fruits)

# # clear()
# fruits.clear()
# print(fruits)
# del fruits
# print(fruits) -> Produces error

# set1 = {1, 0, 2, 3, 4, True, False} '-> Treats True and False as 1 and 0'

# UNION method

# set1 = {1, 2, 3, 4}
# set2= {2, 4, 5, 6}
# set3 = set1 | set2 #set1.union(set2)

# print(set3)

# set1.update(set2)
# print(set1)

# INTERSECTION

# set3 = set1.intersection(set2) # or set1 & set2
# print(set3)
# for updating -> set1.intersection_update(set2)

# Difference

# set3 = set1.difference(set2) # set1 - set2

# # set1.difference_update(set2)
# print(set3)

# SYMMETRIC DIFFERENCE

# set3 = set1.symmetric_difference(set2)
# set3 = set1 ^ set2

# set1.symmetric_difference_update(set2)

# isdisjoint() method
# set1.isdisjoint(set2) #-> Returns True or False

# issuperset()

#set1.issuperset(set2)

# issubset() method
# set2.issubset(set1)




'''
DICTIONARY
'''

# my_dict = {
#     "name": "ram",
#     "roll" : 12,
#     "address": "ktm",
#     "phone_number": [987654321, 9087655443],
#     "marks": [70, 50, 60, 40, 40]
# }

# access

# # print(my_dict["address"])
# print(my_dict.get("address", "ktm"))

# LOOP

# for x in my_dict:
#     print(f"{x} : {my_dict[x]}")

# for x in my_dict.keys():
#     print(x)

# for value in my_dict.values(): -> Accessing values
#     print(value)

# for key, value in my_dict.items():
#     print(key,value)



# ADDING AND UPDATING

# # my_dict["total_marks"] = 100
# my_dict["age"] = 10


# DELETING

# my_dict.pop("age")
# print(my_dict)

# my_dict.clear()
# print(my_dict)

#del my_dict

# no = 9887777
# print(len(no))


'''
NESTED DICTIONARY
'''
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
# print(student["contact"]["phone number"][0])

# for k,v in student.items():
#     if k == "contact" or k == "subject":
#         for key, value in v.items():
#             print(f"{key}: {value}")

# value = student["subject"]
# total_marks = 0
# for v in value.values():
#     total_marks += v

# student["subject"]["total_marks"] = total_marks
# print(student)


'''
FUNCTIONS IN PYTHON
'''

# def calculator (x, y = 0):
#     result = x + y

'''
GLOBAL VARIABLE
'''

# def add():
#     global x
#     x = 20

# add()
# print(x)


'''
ARGS
'''
# def addition(*args): # -> This can take multiple values which will be stored in tuple
#     print(args)

# addition(1, 2, 3, 4, 5)


'''
KWARGS
'''

# def addition(**kwargs):  -> This gives multiple values in dictionary format.
#     print(kwargs)

# addition(name= "ram", roll_no = 19)

# def addition(*args, **kwargs):
#     print(args)
#     print(kwargs)

# addition(1, 2, 3, 4, 5, name = "Ram", age = 20)


'''
RECURSIVE FUNCTIONS
'''

# def fact(n):
#     if n == 0 or n == 1:
#         return 1
    
#     return n * fact(n-1)

# final_result = fact(5)
# print(final_result)

# FIBONACCI SERIES

# def fib(n):
#     if n == 0:
#         return 0
    
#     elif n == 1:
#         return 1
    
#     else:
#         return fib(n-1) + fib(n-2)

# n = int(input("Enter a number: "))

# for i in range(n):
#     print(fib(i), end=" ")

# def sum(n):
#     if n == 0:
#         return 0
#     sum_n = n + sum(n-1)
#     return sum_n

# n = int(input("Enter a number: "))
# sum_n = sum(n)
# print(f"Sum of numbers upto {n} is {sum_n}")

# def arg(*args):
#     print(args)

# arg(1, 2, 3, 4, 5)

# def kwarg(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key} = {value}")

# kwarg(name = "Amrit Sapkota", grade = 12, subject = "Mathematics")


'''
LAMBDA 
'''

# square = lambda x: x ** 2
# print(square(5))

# add = lambda a, b : a + b
# print(add(5, 5))

'''
map()
'''

numbers = [1, 2, 3, 4, 5]

# squared = set(map(lambda x: x**2, numbers))

# print(squared)

def cal(x):
    result1 = x + 1
    result2 = result1 ** 2

    return result2

value = list(map(cal, numbers))
print(value)