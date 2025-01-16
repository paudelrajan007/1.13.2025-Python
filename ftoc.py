#WAP to Convert  celsius to fahrenheit and check whether the man is in fever or normal.

celsius=float(input("Enter Celsius :"))
# Formula °F = °C × (9/5) + 32
fahrenheit= celsius *(9/5)+ 32
temperature=(1)
if temperature in range ( 95,100 ):
    print("Fever :",fahrenheit*temperature)
else :
    print("Normal Temperature :",temperature*fahrenheit)