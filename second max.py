a = [50,40,30,70,5,9,17,90,56,567,2,8,32,65,96]
i = 0
m=0
while i<len(a):
    if a[i]>m:
        m=a[i]
    i+=1       
i =0
m1=0
while i<len(a):
    if a[i]>m1:
        if a[i]!=m:
            m1=a[i]
    i+=1 
print(m1)               
