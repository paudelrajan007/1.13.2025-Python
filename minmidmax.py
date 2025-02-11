x=int(input("Enter a number :"))
y=int(input("Enter a number :"))
z=int(input("Enter a number :"))
min=mid=max=None
if x<y and x<z: #( from this x should be min )
    if y<z:#( from this y should be mid)
        print(x,y,z)
    else:
     print(x,z,y)
     # second condition
elif y<x and y<z: #(From this y should be min)
 if x<z: #(From this x is mid)
   print(y,x,z)
else:
    print(y,z,x)
  #third case
if x<y:
   print(z,x,y)
else:
   print(z,y,x)
   





