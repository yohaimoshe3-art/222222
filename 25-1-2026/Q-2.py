'''
קלוט מהמשתמש:

מספר שורות
מספר עמודות
הדפס מלבן של * לפי המידות

דוגמה: אם נקלטו שורות 3 ועמודות 5 אז הפלט צריך להיות

*****
*****
*****
'''

#START
_lines: int = int(input("enter the number of lines: "))
_cols: int = int(input("enter the number of columns: "))

a= 0
while a < _lines:
    print("*" * _cols)
    a = a + 1
else:
    print("invalid numbers")
#STOP