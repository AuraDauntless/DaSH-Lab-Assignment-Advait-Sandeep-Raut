a=input("what is?")
b=list(a)
c=b[::-1]
print(b)
print(c)
if(b==c):
    print("Palindrome")
else:
    print("Not a Palindrome")