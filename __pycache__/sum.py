total=0
s=input("Enter a number or 'done':")
while s != "done" :
    num=int(s)
    total=total+num
    
    s=input("Enter a number or 'done':")
print("the sum of entered num is ",total)
