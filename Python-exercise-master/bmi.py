name = str(input("請輸入你的名字:"))
weight = int(input("請輸入您的體重:"))
height = int(input("請輸入您的身高:"))
height_m = height / 100
bmi = weight/(height_m ** 2)

if (bmi >= 18.5 and bmi < 24):
    print("{2}{1}{0:.2f}真標準".format(bmi,"您的BMI是:",name))
elif (bmi >= 24 and bmi < 27):
    print("{2}{1}{0:.2f}有點肥".format(bmi,"您的BMI是:",name))
elif (bmi >= 27 and bmi < 30):
    print("{2}{1}{0:.2f}啊啊啊!!要壞掉惹".format(bmi,"您的BMI是:",name))
elif (bmi >= 30 and bmi < 35):
    print("{2}{1}{0:.2f}您是中度肥宅".format(bmi,"您的BMI是:",name))
elif (bmi >= 30 and bmi < 35):
    print("{2}{1}{0:.2f}已經有肥油流出來...".format(bmi,"您的BMI是:",name))
elif (bmi > 35):
    print("{2}{1}{0:.2f}已經有肥油流出來...".format(bmi,"您的BMI是:",name))
else:
    print("{2}{1}{0:.2f}真輕鬆".format(bmi,"您的BMI是:",name))
