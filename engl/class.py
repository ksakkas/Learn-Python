# Class in Python

class mclass:    # class with name mclass
    x = 5        

p1 = mclass()    # Create an object named p1, and print the value of x
print(p1.x)   

print("--------------------")

class Person:
    def __init__(self, name, age):     # The __init__() function is called automatically every time the class is being used to create a new object.
        self.name = name
        self.age = age

p1 = Person("Kostas", 21)

print(p1.name)
print(p1.age)



