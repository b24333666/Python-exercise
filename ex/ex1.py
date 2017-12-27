# for i in range(1,20):
#     for j in range(1,20):
#         print("{}*{}={} \t".format(i,j,i*j),end=' ')
#     print()
F = float(input("攝氏請按c華氏請按F"))
if F == 1:
    F = int(input("請輸入溫度:"))
    def f_to_c(F):
        c = ( F - 32 ) / 1.8
         print("華氏{0:.1f}度=攝氏{0:.1f}度".format(F,c),end=' ')

f_to_c(F)
 
else :
    C = int(input("請輸入溫度:"))
    def f_to_c(c):
            f =  C * 1.8 + 32
            print("攝氏{0:.1f}度=華氏{0:.1f}度".format(C,f),end=' ')

f_to_c(C)


# a = int(input("請輸入溫度:"))
# def f_to_c(x):

#     c = ( x - 32 ) / 1.8
#     print("華氏{0:.1f}度=攝氏{0:.1f}度".format(x,c),end=' ')
# f_to_c(a)

 
b = int(input("請輸入溫度:"))
def f_to_c(c):

    x =  c * 1.8 + 32
    print("攝氏{0:.1f}度=華氏{0:.1f}度".format(c,x),end=' ')

f_to_c(b)