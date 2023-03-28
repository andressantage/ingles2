n=input()
vocal=["a","e","i","o","u"]
debil=["i","u"]
fuerte=["a","e","o"]
g3=["pr","pl","fr","tr","dr","cr","cl","gr","gl","rr","ll","qu","br","ch"]

x=len(vocal)
x1=len(n)
f=[]
a=0
silaba=""
for i in n:
    b=0
    a=a+1
    for j in range(x):
        if vocal[j]==i:
          b=1
    if b==1 and x1!=a:
      silaba=silaba+i+"-"
    elif b==1 and x1==a:
       silaba=silaba+i
    else:
       silaba=silaba+i

x=len(n)-1
#n[j]+n[j+1]
a=0
for j in range(x):
    for i in g3:
        if i==(n[j]+n[j+1]):
            a=1
        break

    
print(a)