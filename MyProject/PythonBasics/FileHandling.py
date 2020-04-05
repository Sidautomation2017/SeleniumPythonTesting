# Text file handling read and write
f = open("Name", "r")
#print(f.read())  # to read all data

# line = f.readline()
# while line != "":
#   print(f.readline(),end="")

#li = f.readlines()  # stores into list
#for line in li:
#    print(line)

# write file
with open("Player", "w") as file:
    li = f.readlines()
    reversed(li)
    for data in reversed(li):
        print(data)
        file.write(data)
f.close()

import xlrd


class ExcelReader:
    loc = 'TestData.xlsx'
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    print(sheet.name)
    print(sheet.cell(0, 1))


a = 3
print("Value of a is ", a)
