#START

pizza = 4
slice_per_pizza = 8
people = 5

#חישוב כמה משולשים יש בסהכ
total_slices = pizza * slice_per_pizza

#חישוב כמה משולשים כל אדם מקבל
slice_per_person = total_slices // people

#חישוב של כמה משולשים נשאר
remaining_slices = total_slices % people

print("every person get", slice_per_person)
print("remaining slices", remaining_slices)

#STOP