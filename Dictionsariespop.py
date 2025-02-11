car={}
length=int(input("Enter length of the dictionary :"))
i=0
while(i<length):
    carname=str(input("Enter car name :"))
    car[carname]="Unknown Model"
    i+=1
    
print(car)
