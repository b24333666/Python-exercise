def f():
    global var
    var = 10
    print(var)
var = 5
f()
print(var)