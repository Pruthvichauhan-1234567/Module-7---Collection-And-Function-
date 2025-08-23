# 6. Write a Python program to sort a list using both sort() and sorted().

numbers = [5, 2, 9, 1, 5, 6]

sorted_numbers = sorted(numbers)
print("Original list after sorted():", numbers)
print("New sorted list using sorted():", sorted_numbers)

numbers.sort()
print("Original list after sort():", numbers)
