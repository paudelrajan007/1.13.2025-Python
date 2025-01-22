# Write a python program to sum of first and last digits of 4 digits numbers.
def sum_of_first_and_last_digits():
    num=int(input("Enter four digits numbers :"))
    first_digit=num//1000
    last_digit=num%10
    sum_of_digits=first_digit+last_digit
    print(f"sum of first digit {first_digit} and last digit {last_digit} is : {sum_of_digits}")
    
sum_of_first_and_last_digits()