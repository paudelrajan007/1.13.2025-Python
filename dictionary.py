Name_Sirname={
    "Rajan":"Paude",
    "Sarbesh":"Shrestha",
    "Amit":"Sing"
}
x=Name_Sirname.keys()
print(x)
Name_Sirname["Pankaj"]="Kori"
print(x)
print(len(Name_Sirname))
print(Name_Sirname)
v=Name_Sirname.values()
print(v)
b=Name_Sirname.items()
print(b)
if "Rajan" in Name_Sirname:
    print("Yes it is in the  dictionary")