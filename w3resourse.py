"word lenght"
# def long_words(n, str):
#     word_len = []
#     txt = str.split(" ")
#     for x in txt:
#         if len(x) > n:
#             word_len.append(x)
#     return word_len	
# print(long_words(3, "The quick brown fox jumps over the lazy dog"))

"diffrence two list"
# list1 = [1, 3, 5, 7, 9]
# list2=[1, 2, 4, 6, 7, 8]
# diff_list1_list2 = list(set(list1) - set(list2))
# diff_list2_list1 = list(set(list2) - set(list1))
# total_diff = diff_list1_list2 + diff_list2_list1
# print(total_diff)
  
"sepret element"
# num = [1, 2, 3, 4, 5]
# print(*num)


# n=["sh","man","sam"]
# print(*n)

"insert aaliment"
# a=[1, 1, 2, 3, 4, 4, 5, 1]
# a.insert(2,12)
# print(a)


# def combination(n, list):
#     if n<=0:
#         yield []
#         return
#     for i in range(len(list)):
#         c = list[i:i+1]
#         for i in combination(n-1, list[i+1:]):
#             yield c + i
# list = [1,2,3,4,5,6,7,8,9]
# n = 2
# result = combination(n, list)
# for e in result:
#     print(e)

"zero of nested list"
# nums = []
# for i in range(3):
#    nums.append([])
#    for j in range(2):
#       nums[i].append(0)
# print("Multidimensional list:")
# print(nums)

# nums = []
# for i in range(3):
#     nums.append([])
#     for j in range(1, 4):
#         nums[i].append(j)
# print("3X3 grid with numbers:")
# print(nums)


# color = ['Red', 'Green', 'Black']
# color = [i for e in color for i in ('c', e)]
# print("Original List: ",color)
# i=100
# d=[]
# while i<=400:
#     s=str(i)
#     if (int(s[0]%2==0)) and (int(s[1]%2==0)) and (int(s[2]%2==0)):
#         d.append(s)
# print(','.join(d))
# i+=1  


# for i in range(7):
#     for j in range(5):
#         if ((j==0 or j==4)and i!=0) or ((i==0 or i==3)and(j>0 and j<4)):
#             print("A", end="")
#         else:
#             print(end=" ")
#     print()                


"largest number"
# def max_num_in_list( list ):
#     max = list[ 0 ]
#     for a in list:
#         if a > max:
#             max = a
#     return max
# print(max_num_in_list([12, 22, -8, 0,-1,-22,34,56,78,98]))

"smallest number"
# def min( list ):
#     min = list[ 0 ]
#     for a in list:
#         if a < min:
#             min = a
#     return min
# print(min([1, 2, -8, 0,-22,-78,-98,1,-1,0,-2,-23,-45]))

"word maching are same ya diffrent"
# def match_words(words):
#   ctr = 0
#   for word in words:
#     if len(word) > 1 and word[0] == word[-1]:
#       ctr += 1
#   return ctr
# print(match_words(['abc', 'xyz', 'aba', '1221',"abcsa","shivis"]))

"largest number"
# a=int(input("enter the number:-"))
# b=int(input("enter the number:-"))
# c=int(input("enter the number:-"))
# if a>b and a>c:
#     print("greater than is",a)
# if b>a and b>c:
#     print("greater than is",b)
# if c>b and c>a:
#     print("greater than is",c)  
# else:
#     print("lesser")          


"split list"
# c=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# step=3
# for i in range(step):
#     print(c[i::step])


# from typing import Counter


# color1 = ["red", "orange", "green", "blue", "white"]
# color2 = ["black", "yellow", "green", "blue"]
# counter1 = Counter(color1)
# counter2 = Counter(color2)
# print(list(counter1 - counter2))
# print(list(counter2 - counter1))




# count = 0
# sum = 0.0
# number = 1
# while number != 0:
# 	number = int(input("enter "))
# 	sum = sum + number
# 	count += 1
# if count == 0:
# 	print("Input some numbers")
# else:
# 	print("Average and Sum of the above numbers are: ", sum / (count-1), sum)
	

# num1=int(input("enter the number:-"))
# num2=int(input("enter the number:-"))
# num3=int(input("enter the number:-"))
# if num1>num2 or num1>num3:
#     print("greater than is",num1)
# if num2>num1 or num2>num3:
#     print("greater than is",num2)
# elif num3>num1 or num3>num2:
#     print("greater than is",num3)  
# else:
#     print("lesser")          


# x=int(input("enter the number:-"))
# y=int(input("enter the number:-"))
# z=int(input("enter the number:-"))
# if x>y>z or z>y>x:
#     print("second maximum num",y)
# elif x>y>y or y>z>x:
#     print("second maximum num",z) 
# else:
#     print("second maximum num",x)       


# def printValues():
# 	l = list()
# 	for i in range(1,21):
# 		l.append(i**2)
# 	print(l[:5])
# 	print(l[-5:])

# printValues()


# s = ['a', 'b', 'c', 'd']
# str1 = ' shivani '.join(s)
# print(str1)

# import collections
# my_list = [10,10,10,10,20,20,20,20,40,40,50,50,30]
# print("Original List : ",my_list)
# ctr = collections.Counter(my_list)
# print("Frequency of the elements in the List : ",ctr)

"prime number"
# n=int(input("enter the number:-"))
# prime_list = []
# for i in range(2, n+1):
#     if i not in prime_list:
#         print (i)
#         for j in range(i*i, n+1, i):
#             prime_list.append(j)
# print(prime_list)


# a=[1,2,3,4,5]
# x=str(' end '.join(map(str,a)))
# print(x)



# a=input("enter the alphabet")
# if len(a)>=6 and len(a)<=16:
#     if a>="A" and a<="Z" or a>="a" and a<="Z":
#         print(a)
#         symbol=input("enter the symbol:-")
#         if symbol in ("@","#","$","&"):
#             print(symbol)
#             num=int(input("enter the number:-"))
#             if num>0 and num<=9:
#                 print(num)
#                 print(a,symbol,num)
#                 print("its strong password")
#             else:
#                 print("not")
#         else:
#             print("wrong")
#     else:
#         print("no")
# else:
#     ("not") 
# 


# word=input("enter the name:-")
# for i in range(len(word)-1,-1,-1):
#     print(word[i],end="")
        

# row=int(input("enter the number:-"))
# col=int(input('enter the number:-'))
# multi=[[1 for j in range(col)]for i in range(row) ]
# # print(multi)
# for i in range(row):
#     for j in range(col):
#         multi[i][j]=i*j
# print(multi)        


# import random
# target_num, guess_num = random.randint(1, 10), 0
# while target_num != guess_num:
#     guess_num = int(input('Guess a number between 1 and 10 until you get it right : '))
# print('Well guessed!')



# Celsius = int(input("Enter a temperature in Celsius: "))

# Fahrenheit = 9.0/5.0 * Celsius + 32

# print ("Temperature:", Celsius, "Celsius = ", Fahrenheit, " F")



# temp = input("Input the  temperature you like to convert? (e.g., 45F, 102C etc.) : ")
# degree = int(temp[:-1])
# i_convention = temp[-1]
# if i_convention.upper() == "C":
#   result = int(9 * degree) // 5+ 32
#   o_convention = "Fahrenheit"
# elif i_convention.upper() == "F":
#   result = int(degree - 32) * 5// 9
#   o_convention = "Celsius"
# else:
#   print("Input proper convention.")
#   quit()
# print("The temperature in", o_convention, "is", result, "degrees.")

# num=input("enter the temperature:-")
# d=int(num[:-1])
# c=num[-1]
# if c=="C":
#   tem = (9 * d) // 5+ 32
#   c="Fahrenheint"
# elif c=="F":
#   tem = (d - 32) * 5// 9
#   c="Celsius"
# else:
#   print("Input proper convention.")
# print("The temperature in", c, "is", tem, "degrees.")


# a=input("enter the number:-")
# d=a.split(",")
# for i in d:
#     if int(str(i),2)%5==0:
#         print(i)
#     else:
#         print("not divisible")    


while True:
    l=input("enter the number:-")
    if l:
        print(l.upper())
    else:
        break




        
    








