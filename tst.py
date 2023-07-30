l=['ABA','PYT','XYZ','MOM','NAN','HANNAH']
c=0
d={}
for i in l:
    c=0
    for j in range (len(i)):
       if i[j] in ['A','E','I','O','U']:
          c+=1
    d[i]=c
print(d)

