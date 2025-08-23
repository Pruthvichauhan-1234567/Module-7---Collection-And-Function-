# 13. Write a Python program to update a value in a dictionary.

# Define a dictionary
employee = {
    "name": "Pruthvi",
    "age": 19,
    "position": "Developer",
    "salary": 50000
}

# Print original dictionary
print("Before update:")
print(employee)

# Update the salary
employee["salary"] = 60000

# Print updated dictionary
print("\nAfter update:")
print(employee)