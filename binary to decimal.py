n=int(input("enter the binary number"))
i=0
final=0
while (n!=0):
    a=n%10
    a=a*2**i
    i=i+1
    final=final+a
    n=n//10
print(final)



