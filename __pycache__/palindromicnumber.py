# palindromic number
Number=int(input("Enter a Number :"))
Original_Number=Number

Reverse=0
while Number >0:
    Num=Number%10
    Reverse=Reverse*10+Num
    Number//=10

print(Reverse)
if Reverse==Original_Number:
    print("Palindromic")

else:
 print("Not Palindromic ")
 