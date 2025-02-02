a=input("Elements separated by space").split()
c=0
for i in range (len(a)):
    a[i]=int(a[i])
    if(c<a[i]):
        c=a[i]
    i+=1
print(c)
d=c
for i in range (len(a)):
    a[i]=int(a[i])
    if(d>a[i]):
        d=a[i]
    i+=1
print(d)
