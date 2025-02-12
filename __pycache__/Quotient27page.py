# Quotient 
# What is a Quotient?
# A quotient is the result obtained when one number is divided by another.
# What is a Quotient? (Easy Explanation) 😊
# A quotient is the answer you get when you divide one number by another.
# # Example 1:
# If you divide 10 by 2:
#  10÷2=5
# Here, 5 is the quotient.
# For example:

# 10 ÷ 3 → Quotient = 3 (integer part) and remainder = 1.
# 15 ÷ 5 → Quotient = 3, remainder = 0.
a=b=c=0
for i in range(1,11):
    a=int(input("Enter num 1:"))
    b=int(input("Enter num 2:"))
    if b==0:
        print("Div by 0 error :")
        break
    else:
        c=int(a/b)
        d=a%b
        print("Quotient=",c)
        print("reminder=",d)
    print("Program error:")