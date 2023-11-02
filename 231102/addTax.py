def addTax(price):
    price = price + 0.1*price
    return price

sum = 0

price = input("please enter the price =" )
while price != "":
    price = float(price)
    print("the product value after adding the tax = ", addTax(price))
    sum = price + sum
    price = input("please enter the price =" )
    
print("the total value after adding the tax = ", sum)