a=input("Numbers separated by space").split()
b=list(a)
c=0
for i in range((len(b))):
    b[i]=int(b[i])
    c=c+b[i]
    i+=1
d=c/len(b)
print("Average of the numbers is",d)




