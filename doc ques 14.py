# num=[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# i=0
# count=0
# a=num[i]
# while i<=len(num): 
#     b=num[i]
#     if b>a:
#         a=b
#     i+=1
#     count+=1 
# print(a,count)  


# num= [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# i=0
# count=1
# mini=num[i]
# while i<len(num) :
#     if len(mini)>len(num[i]):
#         mini=num[i]
#         count+=1
#     i+=1
# print(mini,count)        


# num= [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# i=0
# count=1
# max=num[i]
# while i<len(num) :
#     if len(max)<len(num[i]):
#         max=num[i]
#         count+=1
#     i+=1
# print(max,count)    



a = [2,312,123,3,12,23,12,12]
largest = a[0]
i = 0
while i<len(a):
  if a[i]>largest:
    largest = a[i]
  i = i+1
print (largest)



