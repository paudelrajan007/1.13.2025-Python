#identity operation
# defination The identity operation in Python checks whether two variables reference the same object in memory. It uses the is and is not operators.
# is Returns True if two variables point to the same object in memory
# is not Returns True if two variables do not point to the same object in memory.
a=[1,2,3,3]
b=[1,2,3,3]
x=a
print(a is b)
print(a is x)