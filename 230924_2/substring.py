string = input("please enter your phone number = ")

if string.startswith("+98"):
    print("iran")
elif string.startswith("+1"):
    print("canada")
else:
    print("other")