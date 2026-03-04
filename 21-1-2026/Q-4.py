i = 0

min_rating = 0
max_rating = 0
while i < 10:
    num = int(input("enter a grade to the movie"))

    if num > 5 or num < 1:
        continue

    i = i + 1
    if num > max_rating:
        max_rating = num
    if num < min_rating:
        min_rating = num
print("the min rating to the movie is:", max_rating)
print("the max rating to the movie is:", min_rating)





