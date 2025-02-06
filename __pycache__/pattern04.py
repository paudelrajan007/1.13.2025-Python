#      A
#     ABA
#    ABCBA
#   ABCDCBA
#  ABCDEDCBA
n = 5
for i in range(n):
    spaces = ' ' * (n - 1 - i)
    left = [chr(ord('A') + j) for j in range(i + 1)]
    right = [chr(ord('A') + j) for j in range(i - 1, -1, -1)]
    print(spaces + ''.join(left + right))