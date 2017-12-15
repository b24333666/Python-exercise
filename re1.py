import re
str = "a123456789 z223456789 x343123456 X123456654"
pattern = r"[a-zA-Z]{1}[12]{1}\d{8}"
# id = re.search(pattern,str)
# print(id.group())
ids = re.findall(pattern,str)
print(ids)

strEmail = "wang@gmail.com"
emailPattern = r"^[\w.-]+@[\w.-]+$"
if re.match(emailPattern,strEmail):
    print("{}是正確的email格式".format(strEmail))
else:
     print("{}不正確的email格式".format(strEmail))

print("c:\\python\\uuuuu")
print(r"c:\python\uuuuu")