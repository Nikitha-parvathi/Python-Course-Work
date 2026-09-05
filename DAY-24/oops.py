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


e1 = Employee("Nikitha", 25000)
e1.display()


class Student:
    def __init__(self, name, course):
        self.name = name
        self.course = course

    def display(self):
        print("Name:", self.name)
        print("Course:", self.course)


s1 = Student("Nikitha", "Python")
s2 = Student("Rahul", "Java")
s3 = Student("Priya", "SQL")

s1.display()
s2.display()
s3.display()


class Student:
    college = "Codegnan"

    @classmethod
    def change_college(cls, new_college):
        cls.college = new_college

    @classmethod
    def display(cls):
        print("College:", cls.college)


Student.display()

Student.change_college("ABC Institute")

Student.display()


class Calculator:

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b


print("Addition:", Calculator.add(10, 20))
print("Multiplication:", Calculator.multiply(5, 4))


class Employee:

    company = "ABC Technologies"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # Instance Method
    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)

    # Class Method
    @classmethod
    def company_name(cls):
        print("Company:", cls.company)

    # Static Method
    @staticmethod
    def welcome():
        print("Welcome to the company!")


e1 = Employee("Nikitha", 30000)

e1.display()
Employee.company_name()
Employee.welcome()


class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Student Name:", self.name)
        print("Marks:", self.marks)

    def result(self):
        if self.marks >= 40:
            print("Result: Pass")
        else:
            print("Result: Fail")


s1 = Student("Nikitha", 85)

s1.display()
s1.result()


class Calculator:

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        return a / b


print("Addition:", Calculator.add(10, 5))
print("Subtraction:", Calculator.subtract(10, 5))
print("Multiplication:", Calculator.multiply(10, 5))
print("Division:", Calculator.divide(10, 5))