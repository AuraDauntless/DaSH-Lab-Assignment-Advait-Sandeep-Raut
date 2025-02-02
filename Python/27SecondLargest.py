a=input("What are the elements?(Separate them by a space)").split()
c=0
b=0
for i in range(len(a)):
    a[i]=int(a[i])
    if c<a[i]:
        c=a[i]
a.remove(c)
for i in range(len(a)):
    a[i]=int(a[i])
    if b<a[i]:
        b=a[i]
print(b)