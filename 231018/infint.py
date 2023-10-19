sum = 0

while True:
    try:
        number = int(input("please enter a number = "))
    except ValueError:
        print("please enter a valid value = ")
    else:
        break

while number != -1:
    number = int(number)
    sum = sum + number
    while True:
        try:
            number = int(input("please enter a number = "))
        except ValueError:
            print("please enter a valid value = ")
        else:
            break

print(sum)