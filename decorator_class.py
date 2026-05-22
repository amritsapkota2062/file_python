# Without parameter functionn and without parameter decorator 

# def decorator1(x):

#     def wrapper():
#         print("something before function runs.")

#         x ()

#         print("hi")
#         print("bye")

#     return wrapper

# @decorator1
# def say_hello():
#     print("hello")

# say_hello()

'''With parameter function and without parameter decorator'''
# def decorator1(fun):
#     def wrapper(*args, **kwargs):
#         print("Something before funciton runs.")
#         fun(*args, **kwargs)
#         print("something after the function runs")

#     return wrapper

# @decorator1
# def say_hello(x, y):
#     print("hello", x, y)

# say_hello("abc", "der")


'''With parameter function and with parameter decorator'''

# def great_decorator(greetings):

#     def decorator1(fun):
#         def wrapper(*args, **kwargs):
#             print(f"{greetings} before function runs.")

#             fun(*args, **kwargs)
#             print('Something after function runs.')

#         return wrapper
#     return decorator1

# @great_decorator("hello")
# def say_hello(a, b):
#     print("a and b", a, b)

# say_hello(1, 2)


import time

def execution_time(func):

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time of {end_time - start_time:.4f} seconds")
        return result
    
    return wrapper

@ execution_time
def example_function(n):
    total = 0
    for i in range(n):
        total += i

    return 

example_function(5)