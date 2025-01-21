def num():
    num1=int(input("Enter a number: "))
    print(f"Multiple table of {num1}:")
    for i in range (1,10+1):
        multiply=num1*i
        print(f"{num1} * {i} = {multiply}")

num()
num()