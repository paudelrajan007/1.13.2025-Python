#  Write a python to make basic calculator using if-else statement. 
print("Select operation:")
print("1. Addition : '+' ")
print("2. Subtraction : '-' ")
print("3. Multiplication : '*' ")
print("4. Division : '/' ")
print("5. Modulo : '%' ")
print("6. Exit ")

choice = int(input("Enter your choice (1-6): "))

 
Number_1=int(input("Enter a Number 1 : "))
Number_2=int(input("Enter a Number 2 : "))
if choice==1 :
    Addition = Number_1 + Number_2
    print(Addition)
elif choice==2 :
    
    
    Subtraction = Number_1 - Number_2
    print(Subtraction)
elif choice==3 :
    
    
    Multiplication = Number_1 * Number_2
    print(Multiplication)
elif choice==4 :
    
    
    Division = Number_1 / Number_2
    print(Division)
elif choice==5 :
    
    
    Modulo = Number_1 % Number_2
    print(Modulo)
elif choice==6 :
    
    
    
    print("End")
else:
    print("You have't choose any operation 'Thank you' ")