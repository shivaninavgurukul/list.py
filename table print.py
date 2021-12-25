num=int(input("enter the number:-"))
i=1
d=[]
while i<=num:
    count=1
    while count<=10:
        p=i*count
        d.append(p) 
        # print(i,"*",count,"=",d)
        count+=1   
    # print()    
    i+=1 
print(d)

      