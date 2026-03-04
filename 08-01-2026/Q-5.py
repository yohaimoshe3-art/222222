list1 = ["HELLO", "World", "PYTHON", "code"]
list2 = []
for num in list1:
    if num.isupper():
        reversed_text = num[::-1]
        list2.append(reversed_text)
    else:
        list2.append(num)
print(list2)