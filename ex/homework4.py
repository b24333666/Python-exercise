#4.	列出1到1000中不能被2整除也不能被3整除的數字


print("列出1到1000中不能被2整除也不能被3整除的數字")
for i in range (1,1001):
    if i % 2 !=0 and i % 3 !=0:
        print(i, end=' ')
 
 