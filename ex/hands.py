import random

print("歡迎猜拳")
print("""1.請輸入'剪刀'、'石頭'及'布'中任意一個
2.輸入esc離開""")


name = raw_input("請輸入你的名字:")
print("歡迎% s猜拳"% name)

com = 0
per = 0
draw = 0
while True:
    s = int(random(1,3))
    computer = ("電腦出拳")
    if (s == 1):
        computer = ("剪刀")
    elif (s == 2):
        computer = ("石頭")
    else :
        computer = ("布")
    = raw_input("請出拳:")
