class Parent:
    def display(self):
        print("This is Parent Class")

class Child(Parent):
    def show(self):
        print("This is Child Class")

obj = Child()

obj.display()
obj.show()

class Father:
    def father_property(self):
        print("Father's Property")

class Mother:
    def mother_property(self):
        print("Mother's Property")

class Child(Father, Mother):
    def child_property(self):
        print("Child's Property")

obj = Child()

obj.father_property()
obj.mother_property()
obj.child_property()

class GrandParent:
    def grandparent(self):
        print("Grandparent Class")

class Parent(GrandParent):
    def parent(self):
        print("Parent Class")

class Child(Parent):
    def child(self):
        print("Child Class")

obj = Child()

obj.grandparent()
obj.parent()
obj.child()

class Parent:
    def display(self):
        print("Parent Class")

class Child1(Parent):
    def show1(self):
        print("Child1 Class")

class Child2(Parent):
    def show2(self):
        print("Child2 Class")

obj1 = Child1()
obj2 = Child2()

obj1.display()
obj1.show1()

obj2.display()
obj2.show2()

class A:
    def displayA(self):
        print("Class A")

class B(A):
    def displayB(self):
        print("Class B")

class C(A):
    def displayC(self):
        print("Class C")

class D(B, C):
    def displayD(self):
        print("Class D")

obj = D()

obj.displayA()
obj.displayB()
obj.displayC()
obj.displayD()

class Parent:
    def __init__(self):
        print("Parent Constructor")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child Constructor")

obj = Child()

class Parent:
    def display(self):
        print("This is Parent Method")

class Child(Parent):
    def display(self):
        super().display()
        print("This is Child Method")

obj = Child()
obj.display()
