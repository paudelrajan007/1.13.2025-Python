# A
# AB
# ABC
# ABCD
# ABCDE
character=0
for _ in range (65,70+1):
    for j in range(65,_+1):
        print("\033[31m", chr(j),end=" " "\033[0m")
    print()
