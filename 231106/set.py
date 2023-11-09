clas = ["ali", "hamid", "hosein"]
newClas = set(clas)

newClas.add("hasan")
newClas.add("hasan")
newClas.remove("hosein")
newClas.discard("hosein")
for char in sorted(newClas):
    print(char)