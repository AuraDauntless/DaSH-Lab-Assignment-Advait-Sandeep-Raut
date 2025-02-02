c=input("What is the string?")
a=list(c)
n=input("What is your element?")
b=0
for i in range(len(a)):
    if a[i]==n:
        b+=1
    i+=1
print(b)

