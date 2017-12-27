import random
s = int(random.randint(1, 100))
name = input ("請輸入姓名或按0離開:")
print ("歡迎{} 接受挑戰".format(name))
m = - 1
while s != m:
    str=input("請輸入整數")
    if(str.isdigit()):
        m = int(str)
        if m > s:
            print ("猜大了")
            continue
        elif  m == s:
            print ("真是準")
            break
        elif m < s:
            print ("猜小了")
            continue
        elif m != s:
            print ("請再次輸入1~100之整數")
            continue
        else:
            print("{}太棒了，猜對了".format(name))
            break
        print ("bye")


            
        