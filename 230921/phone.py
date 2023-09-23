phoneNumber = input("please enter your phone number = ")

if phoneNumber.startswith("+"):
    if "+98" in phoneNumber:
        print("IRAN")
    elif "+39" in phoneNumber:
        print("ITALY")
    else:
        print("other")
else:
    print("not valid")