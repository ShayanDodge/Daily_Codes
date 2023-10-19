try:
    number = input("please enter a number = ")
    sum = 0
    while number != "":
        number = int(number)
        sum = sum + number
        number = input("please enter a number again = ")
except ValueError:
    print("please enter correct value")
else:
    print(sum)
finally:
    print("Thank you !")