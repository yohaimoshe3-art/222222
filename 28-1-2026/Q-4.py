#START
i = 1
num_1 = int(input("Enter a number"))
while True:
    num_2 = int(input("Enter a number"))
    if num_2 > num_1:
        i = i + 1
    elif num_2 < num_1:
        i = 1
    num_1=num_2
    if i == 3:
        break
