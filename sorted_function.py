# WAP to take 5 random numbers from users and sort it .
numbers=[]
for num in range(5) :
 number =int(input(f"Enter a number {num + 1}:"))
 numbers.append(number)
 sorted_num=sorted(numbers)
print(sorted_num)