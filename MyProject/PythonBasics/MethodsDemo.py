# instance Methods works with instance variables
# Class Methods works with class variables
# static method will be used when you need do something else apart from class and instance variables

class Student:
    school = "Priyadarshani"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.lap = self.Laptop()
        print("in A student class constructor")

    # instance method
    def avg(self):
        return (self.m1 + self.m2 + self.m3) / 3

    # class method
    @classmethod  # use @classmethod decorator
    def getschoolname(cls):
        return cls.school

    # static method
    @staticmethod  # use @classmethod decorator
    def info():
        print("I am in static method ")

    class Laptop:
        def __init__(self):
            self.brand = "HP"
            self.ram = "8GB"

        def show(self):
            print(self.brand, self.ram)


s1 = Student(4, 5, 6)
print(s1.avg())
print(Student.getschoolname())
Student.info()
lap = s1.lap
lap.show()
