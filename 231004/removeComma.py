number = input("please enter a number (10,000) = ")
location = number.find(",")
print(number[0:location]+number[location+1:])