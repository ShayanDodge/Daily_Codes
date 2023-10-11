with open ("data2.txt" , "r") as infile:
    line = infile.readline()
    country = []
    population = []
    while line != "":
        tempC, tempP = line.split(":")
        country.append(tempC.strip())
        population.append(tempP.strip())
        line = infile.readline()

for i in range(len(country)):
    print(country[i], "=", population[i])