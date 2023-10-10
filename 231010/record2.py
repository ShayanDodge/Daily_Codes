with open ("data2.txt" , "r") as infile:
    line = infile.readline()
    country = []
    population = []
    while line != "":
        temp = line.split(":")
        country.append(temp[0])
        population.append(temp[1])
        line = infile.readline()

for i in range(len(country)):
    print(country[i], "=", population[i])