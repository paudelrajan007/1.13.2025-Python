#  Write a python to make basic calculator using if-else statement.


      
print("Select operation:")
print("1. Addition : '+' ")
print("2. Subtraction : '-' ")
print("3. Multiplication : '*' ")
print("4. Division : '/' ")
print("5. Modulo : '%' ")
print("6. Exit ")
choice = int(input("Enter your choice (1-6): "))
if choice==6:

    print("Exiting... Thank you!")
else:
  Number_1=int(input("Enter a Number 1 : "))
  Number_2=int(input("Enter a Number 2 : "))
  if choice==1 :
    Addition = Number_1 + Number_2
    print(f"{Number_1} + {Number_2} = {Addition}")
  elif choice==2 :
    Subtraction=Number_1-Number_2  
    print(f"{Number_1} - {Number_2} = {Subtraction}")
  elif choice==3 :
    
    Multiplication = Number_1 * Number_2
    print(f"{Number_1} * {Number_2} = {Multiplication}")
  elif choice==4 :
      if Number_2 == 0:
            print("Error! Division by zero is not allowed.")
      else:
        Division = Number_1 / Number_2
        print(f"{Number_1} / {Number_2} = {Division}")
  elif choice==5 :
     if Number_2 == 0:
            print("Error! Modulo by zero is not allowed.")
     else:
       Modulo = Number_1 % Number_2
       print(f"{Number_1} % {Number_2} = {Modulo}")

  else:
    print("You haven't choose any operation 'Thank you' ")



