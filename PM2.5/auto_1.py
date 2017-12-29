import hashlib
import requests
import os

md5 = hashlib.md5()
url = 'http://www.taiwanrate.org/'
md5.update(b'Test string!')
print(md5.hexdigest())

html = requests.get(url).text.encode('UTF-8-sig')
# 判斷網頁是否更新
md5 = hashlib.md5(html).hexdigest()
if os.path.exists('old_md5.txt'):
    with open('old_md5.txt', 'r') as f:
        old_md5 = f.read()
    with open('old_md5.txt', 'w') as f:
        old_md5 = f.write(md5)

else:
    with open('old_md5.txt', 'w') as f:
        f.write(md5)

if md5 != old_md5:
    print("資料已更新...")
else:
    print("資料未更新，正在從資料庫讀取...")