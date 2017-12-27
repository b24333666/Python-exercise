def fun():
    var = 10
    print(var,end=' ')
var = 5
fun()
print(var,end=' ')

def fun():
    global var
    var = 10
    print(var,end=' ')
var = 5
fun()
print(var,end=' ')

var = 50
def fun():
    global var 
    var = 1
    print(var,end=' ')
    #global var = 1
fun()
print(var,end=' ')