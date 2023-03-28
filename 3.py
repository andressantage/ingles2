n="abreviar"
g3=["pr","pl","fr","tr","dr","cr","cl","gr","gl","rr","ll","qu","br","ch"]
c1={"pl":1,"fr":1,"tr":1,"dr":1,"cr":1,"cl":1,"gr":1,"gl":1,"rr":1,"ll":1,"qu":1,"br":1,"ch":1}


x=len(n)-1
#n[j]+n[j+1]
a=0
for j in range(x):
    for i in g3:
        if i==(n[j]+n[j+1]):
            a=1
    if a==1:
        break
print(a)
    
