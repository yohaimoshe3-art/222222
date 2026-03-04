grades = [85, 90, 78, 92, 88]
#Question 1
backup = grades.copy()

#Question 2
grades.clear()

#Question 3
print(f'grades: {grades}')
print(f'backup: {backup}')

#Question 4
extra = [95, 100]
new_grades =backup +extra
print(new_grades)
backup.extend(extra)
print(backup)








