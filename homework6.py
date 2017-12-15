strEmail = "wang@gmail.com"
emailPattern = r"^[\w.-]+@[\w.-]+$"
if re.match(emailPattern,strEmail):
    print("{}是正確的email格式".format(strEmail))
else:
     print("{}不正確的email格式".format(strEmail))