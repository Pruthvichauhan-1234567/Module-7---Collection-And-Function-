# 17. Write a Python program to import the math module and use functions like sqrt(), ceil(), floor().

import math
number = float(input("Enter a number: "))
square_root = math.sqrt(number)
print(f"Square root of {number} is {square_root}")
ceil_value = math.ceil(number)
print(f"Ceil of {number} is {ceil_value}")
floor_value = math.floor(number)
print(f"Floor of {number} is {floor_value}")