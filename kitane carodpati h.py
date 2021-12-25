kitna_paisa_hai = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
i=0
carodpati=0
lakhpati=0
dilwale=0
while i<len(kitna_paisa_hai):
    if  kitna_paisa_hai[i]>=10000000 and i<=1000000:
        carodpati+=1
    elif kitna_paisa_hai[i]>=100000 and i<=10000:
        lakhpati+=1
    else:
        dilwale+=1
    i+=1
print("carodpati",carodpati)
print("lakhpati",lakhpati)
print("dilwale",dilwale)                

