x = 20
for i in range(1, 21):
    if i > x:
        print("i greater than 20 so breaking")
        break
    if i == 10:
        print("don't do anything")
        pass
    else:
        print("value of i", i)

print("bye")
sum1 = 0
for i in range(1, 6, 2):
    print(i)
    sum1 = sum1+i
print(sum1)
