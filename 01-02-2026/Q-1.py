import random
import time
# choose 10 random cards
GREEN_BOLD = '\033[0;32m'
RED_BOLD = '\033[0;31m'
BLUE_BOLD = '\033[0;34m'
YELLOW_BOLD = '\033[0;33m'


player_points = 0
computer_points = 0
for _ in range(25):
    suit : int = random.choice(["❤️", "♦️", "♣️", "♠️"])
    card : int = random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,])

    x : int = random.choice(["❤️", "♦️", "♣️", "♠️"])
    y : int = random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])


    if player_points == 10:
        print(f'{RED_BOLD}You win! with:, {player_points}, points')
        break

    if computer_points == 10:
        print(f'{RED_BOLD}Computer win! with:, {computer_points}, points')
        break

    player_card = card, suit
    computer_card = y, x
    print(f"{GREEN_BOLD}Player card is:", card , suit)
    time.sleep(1)
    print(f"{BLUE_BOLD}Computer card is:", y, x)

    if card > y:
        player_points += 1
        print("player wins the round (+1 point)")
        print(f"{YELLOW_BOLD}score:")
        print("player:", player_points)
        print("computer:", computer_points)
        print("*" * 50)
        time.sleep(1)

    if card < y:
        computer_points += 1
        print("computer wins the round (+1 point)")
        print("score:")
        print("player:", player_points)
        print("computer:", computer_points)
        print("*" * 50)
        time.sleep(1)

    if card == y:
        print("player card:", card, suit)
        print("computer card:", y , x)
        print("Draw - no points awarded")
        continue













