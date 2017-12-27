# Enter the number of rows：10
#        ^
#       ^^^
#      ^^^^^
#     ^^^^^^^
#    ^^^^^^^^^
#   ^^^^^^^^^^^
#  ^^^^^^^^^^^^^
#        ^
#        ^
height = int(input("請輸入層數:"))
L = int(input("請輸入樹幹高:")) 
stars = 1
for i in range(height):
    print((' ' * (height - i)) + ('^' * stars))
    stars += 2
for l in range(L):
    print(' ' *  L  + ('^' * ( stars - (L * 2 ))))