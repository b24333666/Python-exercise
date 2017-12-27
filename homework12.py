# # 12.	請設計一個銀行帳號的類別，有name(姓名)及balance(帳戶餘額)兩個屬性，withdraw()提款、deposit()存款及check_balance()檢查餘額的三個方法。
# # 產生一個銀行帳號的物件時，請列印出 [Hello Jack, 您的開戶金額是NT$100元]
# # 提款時會列印
# # 您提了NT$50元
# # 餘額NT$50元
# # 或
# # 您的存款不足

# # 存款時會列印出
# # 您存了NT$1,000元
# # 餘額NT$1,050元
import time
import random
import uuid

name = input("請入您的姓名: ")
money = int(input("請存入現金開戶: "))    

class bank:
    global firs_bank
    firs_bank = {"name":None,"money":None}

    def __init__ (self,bak):
        self.name = bak['name']
        self.money = bak['money']
        self.id = uuid.uuid1()
    def say_hi(self):
        print ("您好!!{0}先生，開戶帳號為{1}，目前已存款{2}元".format(self.name,self.id,self.money))
 
    def ck(self):
        global x
        x = int(input("{}請按0、{}請按1: ".format("提款","存款")))
        if (x == 0):
            self.pu()
        elif (x == 1):
            self.sa()
        else:
            self.qt

    def pu(self):
            p = int(input("請輸入提款金額: "))
            if (p > self.money):
                print ("餘額不足，目前餘額為: {}元".format(self.money))
            elif  (0 < p and p <=  self.money) :
                self.money -=  p
                firs_bank["money"] = self.money
                print ("提款成功，目前餘額為: {}元".format(self.money))
            else:
                self.b

    def sa(self):
        s = int(input("請輸入存款金額: "))
        if (s > self.money):
            self.money += s
            firs_bank["money"] = self.money
            print ("存款成功，目前餘額為: {}元".format(self.money ))
        else:
            self.b
    def b(self):
        print("取消交易")

    def qt(self):
        while 1:
            self.say_hi()
            if x == 4:
                print('歡迎再度光臨~!!!')
                break



# customer1 = customer(str(input('請輸入姓名:')),int(input('請輸入開戶金額:'))) #姓名、開戶金額
# customer1.welcom() 
# while True:
#     customer1.option()
#     if c == 0:
#         print('Bye~')
#         break

print(firs_bank)        

    


# # for firs_bank in bank_A
# name = input("請入您的姓名: ")
# money = input("請存入現金開戶: ")    
# # count = 0
# # random.choice(account):
#     # account.count += 1

firs_bank["name"] = name
firs_bank["money"] = money
# firs_bank["account"] = account
print(firs_bank)
bank_A = bank(firs_bank)
bank_A.say_hi()

bank_A.ck()
# bank_A.sa()
# bank_A.pu()
# bank_A.b()
# print(firs_bank.values(1))
# class user:
#     # count = 0
#     def __init__ (self,user,age,time,money):
#         self.user = user
#         self.age = age
#         self.time = time
#         self.money = money
#         self.id = uuid.uuid1()
#         # user.count += 1
#     def say_hi(self):
#         print("午安{0}!現在日期為{2}目前{1}歲,您已經存入{3}元整".format(self.user,self.age,self.time,self.money))
#         print("Hello!!{}開戶帳號是{}".format(self.user,self.id))
#     def sandp(say_hi):
#         x = input("{}請按0、{}請按1: ".format(提款,存款))
#         if x = 0:
#             input("請輸入提款金額: ")
#         else:
#             input("請輸入存款金額: ")
            

# user_A = user("楊先生",20,time.strftime("%y/%m/%d"),1000)
# user_A.say_hi()