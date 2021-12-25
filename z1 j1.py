# num=int(input("enter the number"))
# i=1
# while i<=num:
#     print('"'+"q"+str(i)+'"','"'+'z'+str(i)+'"')
#     i+=1


name=str(input("enter the name"))
i=0
d=[]
s=""
while i<=len(name):
    s=str('"',i)
    d.append(s)
    i+=1
print(d)    

