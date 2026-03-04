list1 = [1, 2, 3, 4, 5, 6, 7]
list_even = []
for num in list1:
    if num % 2 == 0:
        list_even.append(num)
list_odd = []
for num in list1:
    if num % 2 != 0:
        list_odd.append(num)
print(f"list odd = {list_odd}")
print(f"list even = {list_even}")