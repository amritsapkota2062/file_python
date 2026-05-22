'''
OOP in Python
'''

# class Person:
#     def __init__(self, name, age):
#         self.name = name 
#         self.age = age

#         def greet(self):
#             return f"Hello, my name is {self.name} and I am {self.age} years old."
        
# person1 = Person("Alice", 30)
# person2 = Person("Bob", 25)

# print(person1.name)
# print(person1.age)

# print(person2.name)
# print(person2.age)

# class Person:
#     def greet(self, name, age):
#         return f"Hello, my name is {name} and I am {age} years old."
# Person1 = Person()
# Person2 = Person()

# value = Person1.greet("Alice", 30)
# print(value)

# class Car:
#     wheels = 4

#     def __init__(self, make, model):
#         self.make = make
#         self.model = model

#     def display(self):
#         return (f"The car was of {self.model} and it is of {self.model} model. It has {self.wheels} wheels")

# car1 = Car("Toyota", "Camry")
# print(car1.display())


'''
INHERITANCE
'''

'''
SINGLE
'''
# class animal:
#     def speak(self):
#         print("Animal speaks")
 
# class dog(animal):
#     def abc(self):
#         print("Dog barks")

# animal1 = animal()
# animal1.speak()

# class rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.breadth
    
# class square(rectangle):
#     def __init__(self, side):
#         self.side = side

#     super().__init__(self.side, self)

class rectangle:
    def area(self, w, l):
        return w * l
    
class square(rectangle):
    def __init__(self, side):
        self.length = side

    def square_Area(self):
        value = super().area(self.length, self.length)
        print("Area of square is: ", value)

box = square(5)

box.square_Area()
print(box.area(5, 10))