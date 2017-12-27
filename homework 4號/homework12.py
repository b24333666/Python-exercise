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
import re

name = input("請入您的姓名: ")
money = int(input("請存入現金開戶: "))
pword = input("請設定密碼: ")

class bank:
    global firs_bank
    firs_bank = {"name":None,"money":None,"password":None,"datatime":time.strftime("%m/%d/%Y")}
    def __init__ (self,bak):
        self.name = bak['name']
        self.money = bak['money']
        self.password = bak['password']
        self.id = uuid.uuid1()
                
    def say_hi(self):
        print ("Hello!!{0}先生，開戶日期為{3}帳號{1}，目前已存款{2}元".format(self.name,self.id,self.money,time.strftime("%m/%d/%Y")))
        
    def ck(self):
        global x
        x = int(input("{}請按0、{}請按1、{}請按2、{}請按3、{}請按9 ".format("提款","存款","查詢餘額","設定密碼",'離開')))
        if (x == 0):
            self.pu()
        elif (x == 1):
            self.sa()
        elif (x == 2):
            self.se()
        elif (x == 3):
            self.pwd()
        else:
            print('歡迎再度光臨~!!!')
            exit()

    def pu(self):
        p = int(input("請輸入提款金額: "))
        while 1:                                    
            if (p > self.money):
                print ("餘額不足，目前餘額為: {}元".format(self.money))
                self.ck()
            elif  (0 < p and p <=  self.money) :
                self.money -=  p
                firs_bank["money"] = self.money
                print ("提款成功，目前餘額為: {}元".format(self.money))
                self.ck()
            else:
                print("取消交易")
                self.ck()
                

    def sa(self):
        s = int(input("請輸入存款金額: "))
        while 1:
            if (s > self.money):
                self.money += s
                firs_bank["money"] = self.money
                print ("存款成功，目前餘額為: {}元".format(self.money ))
                self.ck()
            else:
                print("取消交易")
                self.ck()

    def se(self):
        print ("目前餘額為: {}元".format(self.money ))
        self.ck()

    def pwd(self):
        pw = input("請輸入舊密碼: ")
        matchpword = self.password
        if re.match(matchpword,pw):
            npw = input("請輸入新密碼: ")
            self.password = npw
            nnpw = input("請再次輸入密碼: ")
            matchpword = self.password
            if re.match(matchpword,nnpw):
                print("設定成功即將回到主畫面")
                self.ck()
            else:
                print("設定失敗即將回到主畫面")
                self.ck()
        else:
            print("設定失敗即將回到主畫面")
            self.ck()


firs_bank["name"] = name
firs_bank["money"] = money
firs_bank["password"] = pword
# firs_bank["account"] = account
print(firs_bank)
bank_A = bank(firs_bank)
bank_A.say_hi()
bank_A.ck()
