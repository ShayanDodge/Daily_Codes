number = input("please enter your phone number = ")
if number.isdigit():
    if number.startswith("+98"):
        print("Iran")
    elif number.startswith("+1"):
        print("Canada or USA")
    else:
        print("Others")
elif number.isalpha(): 
    print("please enter a valid value")