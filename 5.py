n="abreviarrafresco"
vocal=["a","e","i","o","u"]
debil=["i","u"]
fuerte=["a","e","o"]
g3=["pr","pl","fr","tr","dr","cr","cl","gr","gl","rr","ll","qu","br","ch"]

c=[]

for i in n:
    c.append(i)
print(c)

x=len(n)-1
agregar=[]
silaba=""

for i in range(x):
    for k in vocal:
        
    for j in g3:
        if j==(n[i]+n[i+1]):
            silaba+="-"

    silaba+=n[i]

print(silaba)
    
    
            






