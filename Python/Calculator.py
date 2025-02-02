print("WELCOME TO CALCULATOR!")
print("(A)ddition,(S)ubtration,(M)ultiplication,(D)ivision\n")
fn=input("What is your function?")
fn=fn.upper()
if (fn=="A"):
    a=float(input("Enter first number"))
    b=float(input("Enter second number"))
    c=a+b
    print("Your Sum Is ", c)
if (fn=="S"):
    a=float(input("What is your minuend?"))
    b=float(input("What is your subtrahend?"))
    c=a-b
    print("Your difference is ", c)
if (fn=="M"):
    a=float(input("What is your first number?"))
    b=float(input("What is your second number?"))
    c=a*b
    print("Your product is ", c)
if (fn=="D"):
    a=float(input("What is your Dividend"))
    b=float(input("What is your Divisor?"))
    c=a/b
    print("Your Quotient is ", c)
elif(fn!="A",fn!="S",fn!="M",fn!="D"):
    print("Invalid Function")

    




