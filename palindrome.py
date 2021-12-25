# a = input("enter the number :-")
# b = a[::-1]
# if(a==b):
#     print("palindrome number")
# else:
#     print("not palindrome")    

# name=["n","i","t","i","n"]
# i=0
# while i<len(name):
#     c=name[-i-1]
#     i+=1
#     print(c)



a=input("enter the string\t")
i=0
rev=a[::-1]
while i<len(a):
    if rev==a:
        print('palindrom',rev)
        break
    else:
        print("not palindrom",rev)
        break



