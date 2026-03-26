import random

def get_random_between_1_10():
    num1 = random.randint(1, 10)
    return num1

def get_random_operation():
    oper = random.choice(['+', '-', '*', '/', '%'])
    return oper

def get_random_between_1_10_number2():
    num2 = random.randint(1, 10)
    return num2

def calc_result(num1, oper, num2):
    if oper == '+':
        return num1 + num2
    elif oper =='%':
        return num1 % num2
    elif oper == '-':
        return num1 - num2
    elif oper == '*':
        return num1 * num2
    elif oper == '/':
        return num1 / num2

num1 = get_random_between_1_10()
oper = get_random_operation()
num2 = get_random_between_1_10()
result = calc_result(num1, oper, num2)

print(f"{num1} {oper} {num2} = ?")
user_result = float(input('whats the result? '))
if result == user_result:
    print('Correct!')
else:
    print(f"Wrong.. the answer was {result}")

