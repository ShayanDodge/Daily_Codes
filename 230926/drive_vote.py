age = int(input("please enter your age = "))

if age > 18:
    print ("you are able to vote and drive.")
elif 16 < age < 18:
    print("you are able to drive.")
else:
    print("you are unable to vote and drive.")
