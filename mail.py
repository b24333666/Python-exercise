# import re
# data = "From:Lenyo Lee (Sales ROW)< Lenyo@jetbrains.com>"
# #str = print(input("請輸入你要找的關鍵字:"))
# #match = re.search(r"str",data)
# match = re.search(r"[\w.-_]+@[\w-]+",data)
# print(match.group())


# data = "From:Lenyo Lee (Sales ROW)< Lenyo@jetbrains.com>"
#str = print(input("請輸入你要找的關鍵字:"))

# import re
# data = str(input("請輸入E-mail格式:"))
# matchmail = "[\w\s.-_]+@[\s\w.]+"
# if re.match(matchmail,data):
#     print("{}{}{}".format("您輸入的E-mail: ",data,"是正確格式"))
# else:
#     print("{}{}{}".format("您輸入的E-mail: ",data,"是錯誤格式"))
#--------------------------------------------------------------------------

x = str(input('請輸入你要找的E-mail:'))
funcname(x)

import re
def funcname(x):
    data = x
    matchmail = "[\w\s.-_]+@[\s\w.]+"
    if re.match(matchmail,data):
        print("{}{}{}".format("您輸入的E-mail: ",data,"是正確格式"))
    else:
        print("{}{}{}".format("您輸入的E-mail: ",data,"是錯誤格式"))
        return

