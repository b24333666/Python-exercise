import random

class SelectBall(object):
    def __init__(self):
        self.run()

    def run(self):
        while 1:
            numStr = input('輸入測試次數:')
            try:
                numl = int(numStr)
                num = numl + 1
            except ValueError:
                print(u'要求輸入一個整數')
                continue
            else:
                break
        ball = [0]*num
        for i in range(num):
            n = random.randint(1,num)
            ball[n-1] += 1
        for i in range(1,num):
            print(u'取得第{}號機率為{}'.format (i,ball[n-1] * 1.0/num))
            # print(u'取得第%d號機率為%f' % (i,ball[n-1] * 1.0/num))

if __name__ == '__main__':
    SB = SelectBall()