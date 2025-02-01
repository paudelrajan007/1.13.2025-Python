#  ABCDE
#  ABCD
#  ABC
#  AB
#  A
j = 69
while j >= 65:
    
    for i in range(65,j+1):
      print(chr(i),end="")
    print()
    j -= 1


''' for j in range(69, 64, -1):  # Loop from 'E' (69) to 'A' (65)
    for i in range(65, j + 1):  # Loop from 'A' (65) to current 'j'
        print(chr(i), end="")  # Print characters on the same line
    print()  # Move to the next line  '''
