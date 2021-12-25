# Given 3 digits a, b, and c. The task is to find all the possible combinations from these digits.
# Examples:
# Input: [1, 2, 3]
# Output:
# 1 2 3
# 1 3 2
# 2 1 3
# 2 3 1
# 3 1 2
# # # 3 2 1
# num=[1,2,3]
# for i in range(3):
#     for j in range(3):
#         for k in range(3):
#                 if (i!=j and j!=k and i!=k):
#                     print(num[i], num[j], num[k])

# num=[1,2,3]
# i=0
# while i<len(num):
#     j=0
#     while j<len(num):
#         k=0
#         while k<len(num):
#             if (i!=j and j!=k and i!=k):
#                 print(num[i],num[j],num[k])
#             k+=1
#         j+=1
#     i+=1            





# num=[1,2,3]
# i=0
# while i<=len(num):
#    print(i)
#    i+=1

# for i in range(-4,5,1):
#     print(i,end="")
#     if i==-1:
#         break

# for i in range(-3,4,1):
#     print(i,end="")
#     if i==-1:
#         break


# for i in range(-3,4,1):
#     print(i,end=" ")
#     if i==1:
#         break


# num=int(input("enter the number:"))

# num=2
# for i in range(1,11):
#     print(i*num)
