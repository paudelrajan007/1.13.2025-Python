# Write a program that ask the user to input num of sec and then expresses it in terms of many min and sec  it contains.
numsec=int(input("Enter num of seconds :"))
num_min=numsec//60
remsec=numsec%60
print("min",num_min)
print("sec",remsec)

