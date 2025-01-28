# WAP to calculate all even and odd number between 100 seprately.

odd=0
even=0

for i in range (1,100+1):
 if i%2==0:
   even=even+i
print(f"Sum of all even number between {i} is : ", even)
for j in range(1,100+1):
  if j%2==1:
    odd=odd+j
print(f"Sum of all odd number between {j} is : ", odd)

