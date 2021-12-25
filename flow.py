# # a = [10,20,30,40,50]
# # i= 0
# # a = 50
# # b = 40
# # a,b = b,a
# # while i<a:
# #     if a>a:
# #         b=a[i]
# #     i+=1
# #  print(b)


# # i=1
# # while i<=5:
# #     print(i)
# #     i=i+1


# # i=1
# # while i<=5:
# #     i=i+1
# #     print(i)



# # i=1
# # while i<=5:
# #     i=i+1
# # print(i)



# # i=1
# # while i<=5:
# #     print(i)
# # i=i+1



# # i=1
# # while i<=5:
# # print(i)
# # i=i+1


# # a =-15
# # b =11
# # print(a//b)



# # name = str(input("enter the name:-")) 
# # if "ing" in name:
# #     print(name+"ly")
# # elif "ly"in name:
# #     print(name+"ing")  
# # else:
# #     print("wrong")      



# # num=int(input("enter the number"))
# # a = (num//1)%10
# # b = (num//10)%10
# # c = (num//100)%10
# # d = (num//1000)%10
# # reverse=(a*1000)+(b*100)+(c*10)+(d*1)
# # if num>1000:
# #     print("reverse")
# # else:
# #     print ("no")   



# # num=int(input("enter the number"))
# # i=1
# # while i<=num:
# #     print('"'+"q"+str(i)+'"','"'+"z"+str(i)+'"')
# #     i+=1



# # i = 1
# # counter = 0
# # while(i<=1000):
# #     if i%1==0:
# #         counter+=1
# #     i+=1
# # if counter==2:
# #     print("prime")
# # else:
# #     print("not")            
   

# i =1
# while i<=1000:
#     sum=0
#     j=0
#     while j>i:
#         if i%j==0:
#             sum+=1
#         i+=1
#     if sum==2:
#         print(i,"p")
#     else:
#         print("n")
#     i+=1         
#     print("all")






num=1
while  (num<=1000):
    count=0
    i=2
    while(i<=num//2):
        if(num%i==0):
            count+=1
        i+=1
    if(count==0 and num!=1):
        print(num,end=" ")
    num+=1        

