from urllib.parse import urlparse
url = 'https://taqm.epa.gov.tw/pm25/tw/PM25A.aspx?area=1'
o = urlparse(url)

print(o)

print("scheme={}".format(o.scheme))
print("netloc={}".format(o.netloc))
print("path={}".format(o.path))
print("params={}".format(o.params))
print("query={}".format(o.query))
print("fragment={}".format(o.fragment))