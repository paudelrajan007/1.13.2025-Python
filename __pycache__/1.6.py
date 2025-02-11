# Python program to print the square root of every alternate number in the range 1 to 10:
# 1, 3, 5, 7, 9
# We start from 1 and then skip one number each time (+2 step).
for i in range(1,11,2):
    print(f"Square root of {i} is {i**0.5 : .2f}") 