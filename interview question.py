a =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
i =4
j=0
while i<len(a):
    if j==0:
      a[i]=15
      j=0
    else:
        a[i]=20
        j=0
    i+=5
print(a)          

