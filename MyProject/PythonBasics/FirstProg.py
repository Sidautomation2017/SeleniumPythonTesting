x = int(input("Enter first number"))
y = int(input("Enter second number"))
z = x + y
print(z)

# ch = input("Enter character")[0]
# print(ch)

# result = eval(input("Enter exp"))
# print(result)
while z > 0:
    if z == 9:
        z = z - 1
        continue
    if z == 4:
        print("Z is equal to 4 ")
        break
    z = z - 1
print("++++++++++")
for x in range(10):
    print(x)
