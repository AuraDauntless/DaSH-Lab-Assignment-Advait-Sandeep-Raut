a=input("Enter the number")
b=list(a)
x=0
for i in range(len(b)): #Navigating the list
    b[i]=int(b[i]) #Conversion of characters
    x=x+b[i]
    i+=1
print(x)

