employees = (
    (101, "Alice", "HR", 55000),
    (102, "Bob", "IT", 72000),
    (103, "Charlie", "Finance", 48000),
    (104, "David", "IT", 80000),
    (105, "Eva", "HR", 50000),
    (106, "Frank", "Finance", 65000)
)

for i in range(0,len(employees)):
    # print(type(employees[i][3]))
    if (employees[i][3]>50000):
        print(employees[i])

print()
hrCount = 0
finCount = 0
ITCount = 0

for i in employees:
    if i[2] == "HR":
        hrCount+=1
    elif i[2]=="Finance":
        finCount+=1
    else:
        ITCount+=1
print("hr ->",hrCount)
print("it ->",ITCount)
print("finance ->",finCount)
print()

maxSalary = employees[0][3]
name = ""
for i in employees:
    if i[3]>maxSalary:
        name = i[1]
        maxSalary = i[3]

print("Maximum salary",maxSalary,name)