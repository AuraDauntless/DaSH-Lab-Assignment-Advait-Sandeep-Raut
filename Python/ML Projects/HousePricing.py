area=[]
price=[]
summation_x=0
summation_y=0
summation_x_squared=0
summation_xy=0

location=input("Where are you looking for a house")
location=str("DBHousePricing/"+location.upper())

for n in range(5):
    a=input("Enter the area and the price in the format (area) (price) ")
    with open (location, 'a') as outputfile:
        outputfile.write(a)
        outputfile.write("\n")
with open (location, 'r')as readfile:
    for line in readfile:
        eachcase=line.strip()
        x,y=eachcase.split()
        area.append(x)
        price.append(y)

enn=len(area)

for i in range(len(area)):
    area[i]=float(area[i])
    summation_x+=area[i]


for j in range(len(price)):
    price[j]=float(price[j])
    summation_y+=price[j]


for p in range(enn):
    area[p]=float(area[p])
    summation_x_squared+=(area[p]*area[p])

for q in range(enn):
    area[q]=float(area[q])
    summation_xy+=(area[q]*price[q])

#print(area) 
#print(price)
#print(summation_x)
#print(summation_y)
#print(summation_x_squared)
#print(summation_xy)

b1=(((enn*summation_xy)-(summation_x*summation_y))/((enn*summation_x_squared)-(summation_x*summation_x)))
avg_x=summation_x/enn
avg_y=summation_y/enn
b0=avg_y-(avg_x*b1)

clienthousearea=float(input("What is the Area of your house?"))
predictedpriceofhouse= b0 + b1*clienthousearea
print("Predicted price of your house is ", predictedpriceofhouse)

with open (location, 'a') as outputfile:
        clienthousearea=str(clienthousearea)
        predictedpriceofhouse=str(predictedpriceofhouse)
        outputfile.write(clienthousearea+" "+predictedpriceofhouse)
        outputfile.write("\n")
