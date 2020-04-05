# Duck Typing
# Operator overloading
# Method overloading
# Method Overriding

# 1. Duck Typing

class PyCharm:
    def execute(self):
        print("compiling")
        print("executing")


class MyEditor:
    def execute(self):
        print("Spell check")
        print("Compiling")
        print("Executing")


class Laptop:
    def code(self, ide):
        ide.execute()


ide = MyEditor()
lap = Laptop()
lap.code(ide)


# 2. Operator Overloading
class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        n1 = self.m1 + other.m1
        n2 = self.m2 + other.m2
        s3 = Student(n1, n2)
        return s3

    def __gt__(self, other):
        m1 = self.m1 + self.m2
        m2 = other.m1 + other.m2
        print("S1 score is ", m1)
        print("S2 score is ", m2)
        if (m1 > m2):
            return True
        else:
            return False

    def __str__(self):
        return '{} {}'.format(self.m1, self.m2)


s1 = Student(48, 69)
s2 = Student(56, 58)

s3 = s1 + s2
print(s3)
print(s3.m2)
if s1 > s2:
    print("S1 wins")
else:
    print("S2 wins")


# Method Overloading
class Employee:

    def sum(self, a=None, b=None, c=None):
        if a != None and b != None and c != None:
            s = a + b + c
        elif a != None and b != None:
            s = a + b
        else:
            s = a
        return s


e = Employee()
x = e.sum(85)
print(x)


# Method Overriding
class A:
    def show(self):
        print("in A show")


class B(A):
    def show(self):
        print("in B show")


b = B()
b.show()
