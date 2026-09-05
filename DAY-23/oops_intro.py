class Student:

    # Class Variable
    college = "MLRITM"

    def __init__(self, name, age):r
        # Instance Variables
        self.name = name
        self.age = age

    def display(self):
        # Local Variable
        course = "Python Full Stack"

        print("Name:", self.name)
        print("Age:", self.age)
        print("College:", Student.college)
        print("Course:", course)

s1 = Student("Nikitha", 24)
s2 = Student("Harsha", 25)

s1.display()
print()

s2.display()