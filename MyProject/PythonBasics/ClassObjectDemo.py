class Student:
    def __init__(self, fn, sn):
        self.x = fn
        self.y = sn
        # self.z

    def add(self):
        z = self.x + self.y
        print(z)

    def compare(self):
        if self.x > self.y:
            print("first number is bigger")
        else:
            print("Second number is big")


stud = Student(4, 3)
stud1 = Student(5, 6)
stud.compare()
stud.add()
print(id(stud))
print(id(stud1))
