def count(*add_all):
    print(add_all)
    count = 0
    for i in add_all:
        count += 1
    return count

print(count(1,2,3,4,5))

def fun1(start,*tu,**di):
    print("start: ", start)
    print("tu: ", tu)
    print("di: ", di)


fun1(1,2,3,a = 4,B = 5)
