import statistics
numbers = [10, 20, 30, 20, 40, 50]
#Question 1
print(numbers.count(20))

#Question 2
print(numbers.index(30))

#Question 3
numbers.append(99)
print(numbers)

#Question 4
numbers.insert(2, 15)
print(numbers)

#Question 5
numbers.remove(20)
print(numbers)

#Question 6
numbers.pop(3)
print(numbers)

#Question 7
print(max(numbers))

#Question 8
print(min(numbers))

#Question 9
print(sum(numbers))

#Question 10
avg = statistics.mean(numbers)
print(f"{avg:.2f}")

#Question 11
print(len(numbers))

