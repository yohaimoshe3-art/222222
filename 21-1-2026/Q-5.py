num = int(input("enter the number of children in the class:"))
i = 0
sum = 0
while i < num:
    grade = int(input("enter the grade:"))
    if grade > 100 or grade < 0:
        continue
    sum += grade
    i += 1
average = sum / num
print("the average is", average)