while 1:
    years = int(input("請輸入西元年份或按0離開:"))
    if (0 != years/4):
        print("西元{0}{1}年份是平年不是閏年,請再輸入一次".format("您輸入的",years))
    elif (100 != years/4):
        quit()        
        print ("西元{0}{1}年份是閏年,謝謝".format("您輸入的",years))
    elif (400 != years/100):
        quit()
        print ("西元{0}{1}年份是平年不是閏年,請再輸入一次".format("您輸入的",years))
    elif (0 == years/400):
        quit()
        print ("西元{0}{1}年份是閏年,謝謝".format("您輸入的",years))
    else:
        break
        print ("感謝輸入!!")



