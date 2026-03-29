import random
cards_deck = [1,2,3,4,5,6,7,8,9,10,"J","Q","K","A"]

print("\n🧍 Player 1 turn")

p1_cards = []
p1_total = 0
p1_disqualified = False
for i in range(2):
    card = random.choice(cards_deck)

    if card in ["J", "Q", "K"]:
        value = 10
    elif card == "A":
        value = 1
    else:
        value = card

    p1_cards.append(card)
    p1_total += value


while True:
    print("Player 1 cards:", p1_cards)
    print("Total:", p1_total)

    if p1_total == 21:
        print("🎯 Player 1 hits 21!")
        break

    if p1_total > 21:
        print("❌ Player 1 disqualified")
        p1_disqualified = True
        break

    choice = int(input("0 = STOP, 1 = CONTINUE: "))

    if choice == 0:
        print("Player 1 stops")
        break

    card = random.choice(cards_deck)

    if card in ["J", "Q", "K"]:
        value = 10
    elif card == "A":
        value = 1
    else:
        value = card

    p1_cards.append(card)
    p1_total += value

print("\n🧍 Player 2 turn")

p2_cards = []
p2_total = 0
p2_disqualified = False
for i in range(2):
    card = random.choice(cards_deck)

    if card in ["J", "Q", "K"]:
        value = 10
    elif card == "A":
        value = 1
    else:
        value = card

    p2_cards.append(card)
    p2_total += value

while True:
    print("Player 2 cards:", p2_cards)
    print("Total:", p2_total)

    if p2_total == 21:
        print("🎯 Player 2 hits 21!")
        break

    if p2_total > 21:
        print("❌ Player 2 disqualified")
        p2_disqualified = True
        break

    choice = int(input("0 = STOP, 1 = CONTINUE: "))

    if choice == 0:
        print("Player 2 stops")
        break

    card = random.choice(cards_deck)

    if card in ["J", "Q", "K"]:
        value = 10
    elif card == "A":
        value = 1
    else:
        value = card

    p2_cards.append(card)
    p2_total += value

print("\n🏁 Final Result")

if p1_disqualified and not p2_disqualified:
    print("Player 2 wins!")
elif p2_disqualified and not p1_disqualified:
    print("Player 1 wins!")
elif p1_disqualified and p2_disqualified:
    print("Both players disqualified – draw!")
else:
    if abs(21 - p1_total) < abs(21 - p2_total):
        print("Player 1 wins!")
    elif abs(21 - p2_total) < abs(21 - p1_total):
        print("Player 2 wins!")
    else:
        print("It's a draw!")
