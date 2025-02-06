fruits=[]
length=int(input("Enter length of list length :"))
for _ in range(1,length+1):
    fruit=str(input(f"Enter {length} fruits : "))
    fruits.append(fruit)
    fruits.sort()
print(fruits)
