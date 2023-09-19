# This program reads, scales, and reverses a sequence of numbers.

def main() :
    numbers = readFloats(5)
    multiply(numbers, 10)
    printReversed(numbers)

def readFloats(numberOfInputs) :
    print("Enter ", numberOfInputs, "numbers: ")
    inputs = []
    for i in range(numberOfInputs) :
        value = float(input(""))
        inputs.append(value)
    return inputs

def multiply (valus, factor) :
    for i in range(len(valus)):
        valus[i] = valus[i] * factor

def printReversed(values) :
    i = len(values) - 1
    while i >= 0:
        print(values[i], end = ", ")
        i -= 1
    
main()




 