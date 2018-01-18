import re
 

x = re.compile("a.*\w")
m = x.match("a9")
print(m)