#完整格式輸出九九乘法表

for i in range(1,10):#for迴圈宣告i進入range(開始值,結束值)
      for j in range(1,10):#for迴圈宣告j進入range(開始值,結束值)
            print('%d*%d=%d'% (i,j,i*j),end = ' ')#顯示(i*j=i*j)
      print ('\n')
print( )

#print '\n'.join(['\t'.join(['%d*%d=%d' % (j,i,i*j) for i in range(1,10)]) for j in range(1,10)]) 