# a=[1,2,3,4,5,66,7,8,9,10]
# i=0
# final=[]
# b=[]
# count=0
# while i<len(a):
#     if count==2:
#         final.append(b)
#         b=[]
#         count=1
#     else:
#         count+=1
#     b.append(a[i])
#     i+=1
# final.append(b)
# print(final)


a=[[1,2],[3,5],[8,9],[12,34],[21,23]]
i=0
d=[]
sum=0
while i<len(a):
    j=0
    while j<len(a[i]):
        d.append(a[i][j])
        sum=sum+a[i][j]
        j+=1
    i+=1
print(d) 
print(sum)   




