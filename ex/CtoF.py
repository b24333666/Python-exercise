def C_to_F(C):
    F = C*1.8 + 32
    print("攝氏{0:.1f}℃轉華氏{0:.1f}℉".format(C,F))

C_to_F(28)


def F_to_C(F):
    C = (F - 32) / 1.8
    print("華氏{1:.1f}℉轉攝氏{0:.1f}℃".format(C,F))

F_to_C(82.4)