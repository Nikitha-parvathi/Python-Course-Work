class Student:
    def __init__(self):
        print("Constructor is called")

s1 = Student()

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

s1 = Student("Nikitha", 25)
s1.display()

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Employee Name:", self.name)
        print("Salary:", self.salary)

e1 = Employee("Rahul", 50000)
e1.display()

class Calculator:
    def add(self, a, b):
        print("Addition =", a + b)

    def sub(self, a, b):
        print("Subtraction =", a - b)

obj = Calculator()
obj.add(10, 20)
obj.sub(20, 10)

class Addition:
    def add(self, a=None, b=None, c=None):
        if a is not None and b is not None and c is not None:
            print(a + b + c)
        elif a is not None and b is not None:
            print(a + b)
        else:
            print(a)

obj = Addition()
obj.add(10)
obj.add(10, 20)
obj.add(10, 20, 30)

class Sum:
    def add(self, *numbers):
        print("Sum =", sum(numbers))

obj = Sum()

obj.add(10)
obj.add(10, 20)
obj.add(10, 20, 30)
obj.add(10, 20, 30, 40)

class Animal:
    def sound(self):
        print("Animals make sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

obj = Dog()
obj.sound()

class Animal:
    def sound(self):
        print("Animal Sound")

class Dog(Animal):
    def sound(self):
        super().sound()
        print("Dog Barks")

obj = Dog()
obj.sound()

class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

n1 = Number(10)
n2 = Number(20)

print("Addition =", n1 + n2)

class Student:
    def __init__(self, marks):
        self.marks = marks

    def __eq__(self, other):
        return self.marks == other.marks

s1 = Student(90)
s2 = Student(90)

print(s1 == s2)

class Student:
    def __init__(self, marks):
        self.marks = marks

    def __gt__(self, other):
        return self.marks > other.marks

s1 = Student(95)
s2 = Student(85)

print(s1 > s2)


















































































































