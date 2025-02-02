n=int(input("What is your number?"))
a=0
x=0
while(a<n):
    a+=1
    b=0
    c=0
    while(b<a):
        b+=1        
        if(a%b==0):
            c+=1
    if(c==2):
        x+=a
print("The sum of all prime numbers is ", x)     

    


