str=str(input("What is your string?"))
l=list(str.upper())
vowels=0
consonants=0
vlist=['A','E','I','O','U']
numbers=['0','1','2','3','4','5','6','7','8','9']
space=['']
for i in range(len(l)):
    if l[i] in vlist:
        vowels+=1
    else:
        consonants+=1
    if l[i] in numbers:
        consonants-=1
    i+=1
print(vowels)
print(consonants)


    


