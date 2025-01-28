number=[]
word=[]
length=int(input("Enter length :"))
for i in range (length):
  numbers=int(input(f"Enter {length} digits numbers :"))
  words=str(input(f"Enter {length} words :"))
  number.append(numbers)
  word.append(words)
  number.sort()
  word.sort()
  sorted_sets=number+word
print("Sorted lists are : ",sorted_sets)

