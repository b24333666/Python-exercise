x = [1,2,3,4,5,6]

y = x

y[3] = 'QQ'
print(x)
print(y)

x = [1,2,3,4,5,6]

y = x[:]

y[3] = 'QQ'
y.insert(4,'哈哈')
print(x)
print(y)