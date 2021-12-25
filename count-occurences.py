list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
i=0
d=[]
while i<len(list):
    j=0
    c=[]
    count=0
    while j<len(list):
        if list[i] in list:
            if list[i]==list[j]:
                count+=1
        j+=1
    c.append(list[i])
    c.append(count)
    if c not in d:
        d.append(c)
    i+=1
        
print(d)
        


