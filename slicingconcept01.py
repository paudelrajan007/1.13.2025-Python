# slicing concept
#def: Accessing parts of a string.
# Given the string random_text = "SharbeshShresthaearn10k$"
"""Seperate the name , salary number and currency """
text="SharbeshShresthaearn10k$"
print("Length of the text :",len(text))
name=text[0 : 15] # it is also written as [ : 15]
salary=text[20 : 23]
currency=text[23 : 24]
print("NAME :", name)
print("salary :", salary)
print("currency :", currency)
