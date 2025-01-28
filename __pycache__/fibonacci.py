# Write a program to print the Fibonacci sequence up to a given number.
# 0,1,1,2,3,5,8,13,21,34,55,89,144,…

# 0+1=1 
# 1+1=2
# 1+2=3
# 2+3=5

num=int(input("Enter a number :"))
print("\n")
a,b=0,1
for i in range(0,num):
    print("The fibonacci is :",a)
    n=a+b
    a=b
    b=n 


                   