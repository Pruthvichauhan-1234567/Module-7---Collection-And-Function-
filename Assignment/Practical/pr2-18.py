# 18. Write a Python program to generate random numbers using the random module.

import random
random_int = random.randint(1, 100)
print(f"Random Integer between 1 and 100: {random_int}")
random_float = random.random()
print(f"Random Float between 0 and 1: {random_float}")
random_uniform = random.uniform(10, 50)
print(f"Random Float between 10 and 50: {random_uniform}")
fruits = ['apple', 'banana', 'cherry', 'mango']
random_choice = random.choice(fruits)
print(f"Randomly selected fruit: {random_choice}")