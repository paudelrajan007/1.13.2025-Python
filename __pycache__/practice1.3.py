#WAP that inputscan intiger in range 0-999 and then print if the integer entered is 1/2/3 digit number.
def i ():

 num=int(input("Enter (0-999) degits number : "))
 if num<0:

    print("invalid number")
 elif num<10:

    print("1 digit num")
 elif num<100:
  print("2 digit num")
 elif num<900:
   print("3 dig")
 else :
  print("4 dig")

i()
i()
i()