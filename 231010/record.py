with open ("data.txt", "r") as infile:
    line = infile.readline()
    country = []
    population = []
    while line != "":
        country.append(line.strip())
        line = infile.readline()
        population.append(line.strip())
        line = infile.readline()
        
for i in range(len(country)):
    print(country[i], "=", population[i])
