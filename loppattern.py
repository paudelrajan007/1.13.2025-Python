# Write a program to print a pattern like a right-angled triangle using nested loops.
 
"""

*
**
***
****
***** 
          
            """
pattern_length=int(input("Enter length of pattern : "))
for r in range (1 , pattern_length + 1) :
    for j in range (r) :
     print("*", end="")
    print()
