number = input("please enter a number = ")
sum = 0
counter = 0

while number != "":
    number=int(number)
    sum = sum + number
    counter = counter +1
    number = input("please enter a number = ")

print(sum/counter)