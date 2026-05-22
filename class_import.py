# import mymodule as m

# print(m.greetings("Hari"))

# from mymodule import greetings

# print(greetings("Amrit"))

# from mymodule import greeting
# 
# s as g
# print(g("Shyam"))

import calculator as c

while True:
    task = c.display_tasks()
    num1 = int(input("Enter num1: "))
    num2 = int(input("Enter num 2: "))

    if task == 1:
        print(c.add(num1, num2))

    elif task == 2:
        print(c.sub(num1, num2))

    elif task == 3:
        print(c.mul(num1, num2))

    elif task == 4:
        print(c.div(num1, num2))

    elif task == 5:
        break

    else:
        print("Enter a valid task!")