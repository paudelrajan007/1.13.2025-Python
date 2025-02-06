fruits=[]
prices=[]
kg=[]


length=int(input("Enter lengtgh of the list :"))
for _ in range (1,length+1):
    fruit=str(input(f"Enter {_} fruits :"))
    price=int(input(f"Enter {_} fruits price :"))
    Kilogram=int(input(f"Enter  kg :"))
    fruits.append(fruit)
    prices.append(price)
    kg.append(Kilogram)

    print(fruits)
    print(prices)
    print(kg)
