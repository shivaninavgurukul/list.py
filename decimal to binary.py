decimal = int(input("enter the number"))
num =""
while decimal!=0:
    num = str(decimal%2)+num
    decimal//=2
print(num)   