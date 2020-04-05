# if you define any variable inside _init_ then it becomes instance variable
# and outside would be treated as Class/static variables
class Car:
    wheels = 4  # class/static varibales

    def __init__(self):
        self.mil = 10 # instance variables
        self.model = "Maruti"

    def add(self):
        z = self.mil  # local variable
        print(z)


c1 = Car()
c2 = Car()
c1.add()
c2.add()
print(c1.wheels)
print(c1.wheels)