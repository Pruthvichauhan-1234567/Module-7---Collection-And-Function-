# 1. Write a Python program to create a list with elements of multiple data types (integers, strings, floats, etc.).

mixed_list=[15,"Pruthvi",22.25,None,True,[1,2,3]]
print("Mixed Data Type List:")
print(mixed_list)

print("Elements Type:")
for item in mixed_list:
    print(f"{item} : {type(item)}")