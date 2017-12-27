print("聯集")
for i in range (1,10):#聯集
    for j in range(1,10,3):
        print("{}|{}={}\t".format(i,j,i|j), end=' ')
    print()

print("對稱差")
for i in range (1,10):#對稱差
    for j in range(1,10,3):
        print("{}^{}={}\t".format(i,j,i^j), end=' ')
    print()

print("差集")
for i in range (1,10):#差集
    for j in range(1,10,3):
        print("{}-{}={}\t".format(i,j,i-j), end=' ')
    print()
    
print("交集")
for i in range (1,10):#交集
    for j in range(1,10,2):
        print("{}&{}={}\t".format(i,j,i&j), end=' ')
    print()