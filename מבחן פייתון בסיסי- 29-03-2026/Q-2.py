
def find_median(numbers: list) -> float | None:
    if not numbers:
        return None

    sorted_numbers = sorted(numbers)
    length = len(sorted_numbers)

    if length % 2 == 1:
        return float(sorted_numbers[length // 2])
    elif length % 2 == 0:
        return float(sorted_numbers[length // 2 - 1] + sorted_numbers[length // 2]) / 2

nums = []
while True:
    user_input = input("enter a number: ")

    if user_input == "Done":
        break

    try:
        nums.append(int(user_input))
    except ValueError:
        print('please enter a valid number')

result = find_median(nums)
if result == None:
    print("No numbers entered")
else:
    print(f'the median of the your list is: {result}')