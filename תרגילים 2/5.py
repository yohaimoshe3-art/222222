import time

RED_BOLD = "\033[0;31m"
BLUE_BOLD = "\033[1;34m"
GREEN_BOLD = "\033[0;32m"
YELLOW_BOLD = "\033[1;33m"
PURPLE_BOLD = "\033[1;35m"
ORANGE_BOLD = "\033[0;33m"
print(f"{YELLOW_BOLD}=" * 50)
print(f"{RED_BOLD}welcome to the game".center(50))
print(f"{BLUE_BOLD}Zohar the queen and Yohai moshe the king".center(50))
print(f"{YELLOW_BOLD}=" * 50)
incorrect_member = 0
score_member = 0
level_game = input(f"{GREEN_BOLD}do you want a hard level? or easy level?")
if level_game == "easy" :
    print(f"{YELLOW_BOLD}*" * 50 )
    print(" " *50)
    print("you have chosen easy game: good luck!")
    print(" " *50)
    print(f"{YELLOW_BOLD}*" * 50)
    print(" " *50)
    time.sleep(1)



    question_1 = input(f"{BLUE_BOLD}what is 8 + 5?")
    if question_1 == "13":
        print(f"{RED_BOLD}your right! good job")
        print(" " * 50)
        print(f"{YELLOW_BOLD}*" * 50)
        print(" " * 50)
        score_member += 1

    else:
        print(f"{RED_BOLD}Maybe next time...")
        print(" " * 50)
        print(f"{YELLOW_BOLD}*" * 50)
        print(" " * 50)
        incorrect_member += 1
    time.sleep(1)


    question_2 = input(f"{BLUE_BOLD}what is 69+37?")
    if question_2 == "106":
        print(" " *50)
        print(f'{PURPLE_BOLD}great job🥳😍!')
        print(" " *50)
        print(f"{YELLOW_BOLD}*" * 50)
        score_member += 1
    else:
       print(f"{PURPLE_BOLD}Maybe next time...")
       print(" " * 50)
       print(f"{YELLOW_BOLD}*" * 50)
       print(" " * 50)
       incorrect_member += 1

    time.sleep(1)

    question_3 = input(f"{BLUE_BOLD}what is 18 x 9?")
    if question_3 == "162":

        print(" " *50)
        print(f'{PURPLE_BOLD}wow! keep going🥳')
        print(" " *50)
        print(f"{YELLOW_BOLD}*" * 50)
        score_member += 1
    else:
        print(f"{PURPLE_BOLD}Maybe next time...😓")
        print(" " * 50)
        print(f"{YELLOW_BOLD}*" * 50)
        print(" " * 50)
        incorrect_member += 1

    question_4 = input(f"{BLUE_BOLD}what is 171:9 ?")
    if question_4 == "19":
        print(" " *50)
        print(f'{PURPLE_BOLD}great job👌🥳!')
        print(" " *50)

        score_member += 1
    else:
        print(f"{PURPLE_BOLD}Maybe next time...🥱")
        print(" " * 50)
        print(f"{YELLOW_BOLD}*" * 50)
        print(" " * 50)
        incorrect_member += 1

    print(f"{YELLOW_BOLD}*" * 50)
    print(" " * 50)
    print(f"{BLUE_BOLD}your correct answers is....🥁🥁🥁:")
    time.sleep(2)
    print(f"{score_member} " "🏆")
    print(" " * 50)
    print("your incorrect answers is....")
    time.sleep(1)
    print(f'{incorrect_member} 🤒')

else:
    score_user = 0
    incorrect_user = 0
    print(f"{YELLOW_BOLD}*" * 50)
    print(" " * 50)
    print("you have chosen hard level: good luck!")
    print(" " * 50)
    print(f"{YELLOW_BOLD}*" * 50)
    print(" " * 50)
    time.sleep(1)
    qustion_num_1 = input(f"{BLUE_BOLD}what is '5!'?")
    if qustion_num_1 =="120":
        print(" " * 50)
        print(f'{PURPLE_BOLD}great job🥳😍!')
        print(" " * 50)
        print(f"{YELLOW_BOLD}*" * 50)
        score_user += 1
    else:
        print(f"{PURPLE_BOLD}Maybe next time...")
        print(" " * 50)
        print(f"{YELLOW_BOLD}*" * 50)
        print(" " * 50)
        incorrect_user += 1
    qustion_num_2 = input(f"{BLUE_BOLD}what is 4**2 + 3!, ")
    if qustion_num_2 =="22":
        print(" " * 50)
        print(f"{YELLOW_BOLD}*" * 50)
        print(" " * 50)
        print(f'{PURPLE_BOLD}great job🥳😍!')
        print(" " * 50)
        print(f"{YELLOW_BOLD}*" * 50)
        score_user += 1
    else:
        print(f"{PURPLE_BOLD}Maybe next time...")
        print(" " * 50)
        print(f"{YELLOW_BOLD}*" * 50)
        print(" " * 50)
        incorrect_user += 1
    qustion_num_3 = input(f"{BLUE_BOLD}what is (10-2)**3, ")
    if qustion_num_3 =="2":
        print(" " * 50)
        print(f'{PURPLE_BOLD}great job🥳😍!')
        print(" " * 50)
        print(f"{YELLOW_BOLD}*" * 50)
        score_user += 1
    else:
        print(f"{PURPLE_BOLD}Maybe next time...")
        print(" " * 50)
        print(f"{YELLOW_BOLD}*" * 50)
        print(" " * 50)
        incorrect_user += 1

    print(f"{YELLOW_BOLD}*" * 50)
    print(" " * 50)
    print(f"{BLUE_BOLD}your correct answers is....🥁🥁🥁:")
    time.sleep(2)
    print(f"{score_user} 🏆")
    print(" " * 50)
    print("your incorrect answers is....")
    time.sleep(1)
    print(f'{incorrect_user}" " 🤒')


















