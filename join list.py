# a=[1,2,3]
# b=[4,5,6]
# c=[7,8,9]
# d=a+b+c
# print(d)



# my_list = [1, 2, 3, 1, 2, 4, 5, 4 ,6, 2]
# temp_list = []
# for i in my_list:
#     if i not in temp_list:
#         temp_list.append(i)
# my_list = temp_list
# print("List After removing duplicates ", my_list)


my_list = [1, 2, 3, 1, 2, 4, 5, 4 ,6, 2]
temp_list = []
i=0
while i<len(my_list):
    if my_list[i] in temp_list:
        pass
    else:
        temp_list.append(my_list[i])
    i+=1
print(my_list)    
print(temp_list)        