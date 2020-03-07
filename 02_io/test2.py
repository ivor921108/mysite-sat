def read():
    cut = int(input())
    print(cut)
    for i in range(cut):
     x = int(input())
     str1='input'+str(i+1)+':'
     str2='sqrt'+str(i+1)+':'
     print(str1,x,str2,round(x**0.5,3))
     
read()