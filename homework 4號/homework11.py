# 讓使用者輸入身高、體重、腰圍及性別
# 根據身高及體重算出BMI，18.6 >= BMI < 24
# 或男性腰圍<90、女性腰圍<80
# 就列印出健康，否則就列印出不健康

def BMI():
    x = float(input('請輸入身高(m):' ))
    y = int(input('請輸入體重(kg):' ))
    global b
    b = float( y / (x ** 2))

def W():
    global w
    w = int(input('請輸入腰圍(cm):' ))
    
    
sex = int(input('請輸入性別(男0、女1):' ))
BMI()
W()

while 1 :
    
    if sex == 0 :
        if b >18.6 and b < 24 and w < 90:
            print("健康")
            break
        else:
            print("不健康")
            break


    if sex == 1 :
        if b >18.6 and b < 24 and w < 80:
            print("健康")
            break
        else:
            print("不健康")