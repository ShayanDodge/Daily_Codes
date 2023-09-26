command = input ("please enter your command = ")

match command:
    case "hello":
        print("hello to you too!")
    case "goodbye":
        print("see you later!")
    case other:
        print("I have no information!")