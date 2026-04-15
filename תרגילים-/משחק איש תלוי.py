import random

# in python we write in upper case constant (not changed during run)
CAPITAL_CITIES = [
    "TOKYO", "PARIS", "LONDON", "BERLIN", "MADRID",
    "ROME", "VIENNA", "PRAGUE", "WARSAW", "ATHENS",
    "CAIRO", "ANKARA", "BEIJING", "SEOUL", "HANOI",
    "BANGKOK", "CANBERRA", "OTTAWA", "BRASILIA", "BUENOS AIRES"
]

city = random.choice(CAPITAL_CITIES)
guesses_set = set()

while True:
    print('_' * len(city))
    while True:
        guess = input('Enter your guess: ').upper()
        is_alpha = guess.isalpha()
        if guess not in guesses_set:
            continue
        if len(guess) == 1:
            continue
        if is_alpha:
            continue
        else:
            break
    guesses_set.add(guess)
    if guess in city:
        city = "".join(city)
        x = city.find(guess)


        city = city.replace("_", guess)
        city























