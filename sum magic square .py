magic_square = [
[8, 3, 4],
[9, 5, 1],
[6, 7, 2]
]
i=0
while i<len(magic_square):
    j=0
    sum=0
    while j<len(magic_square[i]):
        sum+=magic_square[i][j]
        j+=1
    i+=1
print("sum of row:",sum)
d=0
while d<len(magic_square):
    p=0
    sum1=0
    while p<len(magic_square[d]):
       sum1+=magic_square[d][p]
       p+=1
    d+=1
print("sum of colouns:",sum1)
t=0
n=t
sum2=0
while t<len(magic_square):
    sum2=sum2+magic_square[n][t]
    t+=1
print("sum of diagonals:",sum2)    

                
