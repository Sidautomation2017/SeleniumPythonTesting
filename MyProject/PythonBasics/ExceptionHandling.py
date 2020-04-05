itemsinCart = 0
x = 2

if itemsinCart != 2:
    pass

try:
    y = x / 0
    #file = open("testr")
    #print(sum())

except ArithmeticError:
    print("Arithmatic error")
except FileNotFoundError as e:
    print("Filenot founf", e)
except Exception as e:
    print("parent exception",e)
