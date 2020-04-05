class A:
    def __init__(self):
        print("in A init")

    def function1(self):
        print(" I am in function1")

    def function2(self):
        print("I am in function2")


class B:
    def __init__(self):
        print("in B init")
    def function1(self):
        print("I am in functionb1")

    def functionb(self):
        print("I am in functionb")


class C(B,A):
    def __init__(self):
        super().__init__()
        print("In C init")
    def function4(self):
        print("I am in function4")

    def function5(self):
        print("I am in function5")


a = A()
b = B()
c = C()
c.__init__()
