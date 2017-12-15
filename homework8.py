import re
str = "0911-222-333 0911222333 0955811123 0815-676-480"
pattern = "[09]{2}[\d]{2}-[\d]{3}-[\d]{3}"
ids = re.findall(pattern,str)
print(ids)