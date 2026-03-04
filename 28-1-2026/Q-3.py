valid_players = 0
above_16 = 0

for i in range(10):
    age = int(input("הכנס גיל שחקן: "))

    if age < 12:
        continue

    if age > 18:
        print("שחקן מבוגר מדי – עצירת הקליטה")
        break

    valid_players += 1

    if age > 16:
        above_16 += 1

print("מספר שחקנים תקינים:", valid_players)
print("מספר שחקנים מעל גיל 16:", above_16)

