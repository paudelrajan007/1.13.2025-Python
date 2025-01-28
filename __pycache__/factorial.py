# Write a program to find the factorial of a number.
factorial=1
for i in range(-5,-1+1):
    for j in range(-5,-1+1):
        king=i*j
    factorial*=king
        
print("factorial is :",factorial)
