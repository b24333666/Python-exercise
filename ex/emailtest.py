# import re
# x = str(input('請輸入你要找的E-mail:'))

# def funcname(x):
#     data = x
#     matchmail = "[\w\s.-_]+@[\s\w.]+"
#     if re.match(matchmail,data):
#         print("{}{}{}".format("您輸入的E-mail: ",data,"是正確格式"))
#     else:
#         print("{}{}{}".format("您輸入的E-mail: ",data,"是錯誤格式"))
#         return

# funcname(x)

import re
x = str(input("請輸入你的E-mail格式: "))

def funmail(x):
    date = x
    matchmail = "[\s\w._]+@[\w\s.]+"
    if re.match(matchmail,date):
        print("{}{}{}".format("您輸入的E-mail: ",date,"正確的"))
    else:
        print("{}{}{}".format("您輸入的E-mail: ",date,"錯誤的"))

funmail(x)

