def display_tasks():
    task = int(input("What do you want to do?\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. EXit"))
    return task

def add(num1, num2):
    result = num1 + num2 
    return f"{num1} + {num2} = {result}"

def sub(num1, num2):
    result = num1 - num2 
    return f"{num1} - {num2} = {result}"

def mul(num1, num2):
    result = num1 * num2 
    return f"{num1} * {num2} = {result}"

def div(num1, num2):
    result = num1 / num2 
    return f"{num1} / {num2} = {result}"