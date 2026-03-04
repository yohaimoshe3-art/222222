i = 0
sum = 0

while True:
    num = int(input("enter a number: "))
    if num == -999:
        break
    elif num != -999:
        sum += num
        i = i + 1
print(sum)
print(i)

