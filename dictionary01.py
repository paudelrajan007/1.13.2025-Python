name_sirname={}

list=int(input("Enter dict length :"))
for _ in range(1,list+1):
 nam=str(input("Enter Name :"))
 sirnam=str(input("Enter Sir Name :"))
 name_sirname.update({nam:sirnam})
print(name_sirname)
