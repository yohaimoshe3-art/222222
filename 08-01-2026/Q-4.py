list1 = ["Hello world",
         "Python is fun",
         "I love coding"]
list2 = []
for num in list1:
    split_word = num.split()
    for word in split_word:
        list2.append(word)

print(list2)