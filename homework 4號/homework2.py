# 判斷第幾象限?
# 讓使用者自行輸入x,y的座標
# 1.x>0 且 y>o 在第一象限
# 1.x<0 且 y>o 在第二象限
# 1.x<0 且 y<o 在第三象限
# 1.x>0 且 y<o 在第四象限
x = int(input("請輸入X座標或按0離開:"))
y = int(input("請輸入Y座標或按0離開:"))
while 1:
    if ( x>0 and y>0):
        print("{0}座標是{1},{2}在第一象限".format("您輸入的",x,y))
    elif (x>0 and y<0):
        print("{0}座標是{1},{2}在第二象限".format("您輸入的",x,y))
    elif (x<0 and y<0):
        print("{0}座標是{1},{2}在第三象限".format("您輸入的",x,y))
    elif (x<0 and y>0):
        print("{0}座標是{1},{2}在第四象限".format("您輸入的",x,y))
    else:
        print ()
        break
    print ("感謝輸入!!")
