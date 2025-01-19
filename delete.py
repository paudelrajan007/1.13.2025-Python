# Remove items from a list while iterating.
num=[]
for number in range(6):
    numbers=int(input(f"Enter the numbers {number +1 } :"))
    num.append(numbers)
print("Before sorting numbers are :",num)
sorte=sorted(num)
print("After sorting numberds are :",sorte)
while True:
    delete=int(input("Enter the number you want to delete : or (enter -1 if you want to end):"))
    if delete == -1:
     break
    if delete in sorte :
        sorte.remove(delete)
        print(f"{delete} has been removed updated list is :",sorte)
    else :
        print("The number is not found in the list :")

