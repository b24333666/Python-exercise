# 9.	讀取下列list中的資料
# list1 = [[“a”,”b”,”c”],[1,2,3,4],[“x”,”y”,”z”]]

list1 = [["a","b","c"],[1,2,3,4],["x","y","z"]]

for i in list1:
    for j in i:
        print(j,end=' ')
    print()
