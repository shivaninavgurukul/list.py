# a=[[1,2,4],[3,4,5],[6,7,8]]
# d=[]
# for i in a:
#     d.append(i[0]+i[1])
# print(d)

# a=[[1,2],[3,5],[7,8],[6,9],[4,2]]
# i=0
# sum=0
# while i<len(a):
#     j=0
#     while j<=i-i:
#         sum+=a[i][j]
#         j+=1
#     i+=1
# print(sum)        

# a=[[1,2],[3,5],[7,8],[6,9],[4,2]]
# i=0
# d=[]
# sum=0
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         d.append(a[i][0]+a[i][1])
#         break
#     i+=1
# print(d)        

# a=[[1,2,4],[3,5,4],[7,8,6],[6,9,7],[4,2,1]]
# i=0
# d=[]
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         d.append(a[i][0]+a[i][1])
#         break
#     i+=1
# print(d)        



# a=[1,2,3,4,[6,8],[7,[1,2],8,9,5,7],1,2,3,4,5,6,[56,34,23],76,43]
# i=0
# sum=0
# while i<len(a):
#     if type(a[i])==list:
#         j=0
#         while j<len(a[i]):
#             if type(a[i][j])==list:
#                 k=0
#                 while k<len(a[i][j]):
#                     sum+=a[i][j][k]
#                     k+=1
#             else:
#                 sum+=a[i][j] 
#             j+=1
#     else:
#         sum+=a[i]
#     i+=1
# print(sum)                           