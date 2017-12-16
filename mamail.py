import re
data = str(input("請輸入E-mail格式:"))
matchmail = r"[\w\s.-_]+@[\s\w.]+"
if re.match(matchmail,data):
    print("{}{}{}".format("您輸入的E-mail: ",data,"是正確格式"))
else:
    print("{}{}{}".format("您輸入的E-mail: ",data,"是錯誤格式"))

