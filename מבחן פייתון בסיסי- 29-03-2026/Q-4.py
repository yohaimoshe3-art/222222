list1 = []
while True:
        user_input = input('enter string: ').lower()
        if user_input == 'quit':
            break
        elif user_input.isalpha():
            list1.append(user_input)
        else:
            print('please enter only string')

new_list = list1

set1 = set(new_list)

if len(set1) < len(new_list):
    print("There were duplicate")
elif len(set1) == len(new_list):
    print("There were duplicate")








