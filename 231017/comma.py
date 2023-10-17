number = input("please enter a number = ")
index = number.find(",")
print(index)
print(number[0:index]+number[index+1:])