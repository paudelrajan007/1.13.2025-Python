# Multiplication Table: Create a program that generates and prints the multiplication table for a number provided by the user using a while loop.
def multiple (num):
    count=1
    while count <=10 :
     table=count*num
     print(f"{num} * {count} = {table} ")
     count +=1

num=int(input("Enter a number :"))
multiple(num)

