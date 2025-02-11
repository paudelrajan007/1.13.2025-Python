Dictionaries={
    "Apple":"Price=>200kg",
    "Banana":"Price=>70kg",
    "Mango":"Price=>180kg"

}
print(len(Dictionaries))
print(Dictionaries)
print(type(Dictionaries))
fruitsandprice=dict(apple="Price=>200kg", Banana="Price=>70kg",Mango="Price=>180kg")
print(fruitsandprice)
print(type(fruitsandprice))
print(len(fruitsandprice))
x=fruitsandprice["apple"]
print(x)
a=fruitsandprice.get("apple")
print(a)
v=fruitsandprice.keys()
print(v) 