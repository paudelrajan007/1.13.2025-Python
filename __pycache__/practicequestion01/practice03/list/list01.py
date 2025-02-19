fruits=[]
for i in range (1,8):
    fruit=str(input(f"Enter {i} names :"))
    fruits.append(fruit)
    fruits.sort()
print(fruits)