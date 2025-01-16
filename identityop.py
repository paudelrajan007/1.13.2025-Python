# Using is
x = [1, 2, 3]
y = x       # y references the same object as x
z = [1, 2, 3]  # z is a different object with the same content

print(x is y)   # True (same object)
print(x is z)   # False (different objects with same content)

# Using is not
print(x is not z)  # True

# Identity with immutable types (like integers)
a = 100
b = 100
print(a is b)  # True (small integers are cached)

c = 1000
d = 1000
print(c is d)  # False (large integers are not cached)
