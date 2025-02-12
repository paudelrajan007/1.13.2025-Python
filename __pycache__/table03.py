# for row in range(1,10):
#     for col in range(1,10):
#         prod=row*col
#         if prod <10:
#          print('',prod,'',end="")
#         else:
#          print(prod,'',end="")
# print()
for row in range(1, 10):
    for col in range(1, 10):
        prod = row * col
        print(f"{prod:2}", end=" ")  # Right-aligns numbers for better formatting
    print()  # Moves to the next line after each row
