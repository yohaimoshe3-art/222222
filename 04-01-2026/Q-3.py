time = int(input("enter the time in minutes to took the restaurant to bring the meal: "))
price = float(input("enter the price of the meal: "))
is_quick_service : bool = time < 15
is_expensive : bool = price < 100
if is_quick_service:
    print(is_quick_service)
else:
    print(is_quick_service)

if is_expensive:
    print(is_expensive)
else:
    print(is_expensive)

if is_quick_service and not is_expensive:
    print("recommended")
else:
    print("not recommended")