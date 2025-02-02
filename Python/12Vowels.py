a=input("What is your string?")
b=list(a)
c=0
vowels=['a','e','i','o','u','A','E','I','O','U']
for i in range(len(b)):
    if a[i] in vowels:
        c+=1
    i+=1
print(c)