name = input("please enter a name = ")
if len(name) % 2 == 1:
    index = (len(name)-1)/2
    index = int(index)
    print(name[index])
else:
    index = (len(name))/2
    index = int(index)
    print(name[index-1:index+1])