# def f(L, N=set()): # it's bad
def f(L, N=None):
    # print L,f.N
    if N is None:
        N = set()
    if not L:
        return []
    elif L[0] in N:
        return f(L[1:],N)
    elif L[0] in L[1:]:
        return f(L[1:],N|{L[0]})
    else:
        return [L[0]]+f(L[1:],N)


if __name__=='__main__':
    A = [9,5,5,4,7,6,4,1,2,0,10,9,7]
    print f(A)
    # [6, 1, 2, 0, 10]  