name = input("please enter your name = ")
name = name.strip()
name = name.replace("a", "@")
print(name[0].upper()+name[1:].lower())
print(name.find("@"))
print(name.startswith("@"))
print(name.endswith("i"))