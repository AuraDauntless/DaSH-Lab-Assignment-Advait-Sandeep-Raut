a=input("what is?")
b=list(a)
c=b[::-1]
for i in range(len(b)):
    b[i]=int(b[i])
    i+=1
for j in range(len(c)):
    c[j]=int(c[j])
    j+=1
print(b)
print(c)
if(b==c):
    print("Palindrome")
else:
    print("Not a Palindrome")
    

