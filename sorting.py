
def sorting ():
    num=[]
    length=int(input(" Enter a length : "))
    for i in range(length ):
        number=int(input(f"Enter number {i+1} : "))
        num.append(number)
    print(f" Before sorting : {number +1} ")
    num.sort()
    print(f"After sorting : {num}")

sorting()

