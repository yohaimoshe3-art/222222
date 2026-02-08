
#START
i=0
good = 0
over_16 = 0
while (i <= 10):
     age = int(input("Enter age"))
     i = i+1
     if age > 18:
        break
     if age > 16:
         over_16 = over_16 + 1
     if age <= 18 and age >=12:
        good = good+1
print("גילאים תקינים", good)

print("מעל גיל 16", over_16)
#START

