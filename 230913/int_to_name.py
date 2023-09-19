# This program will turn an integer lower than 1000 into it's English name.

def main() :
    value = int(input("please enter a positive integer that is lower than 1,000 = "))
    print(intname(value))

def intname(number) :
    part = number 
    name = ""

    if part >= 100 : 
        name = digitName (part // 100) + " hundrad"
        part = part % 100
    if part >= 20 :
        name = name + " " + tyName (part)
        part = part % 10
    elif part >= 10 :
        name = name + " " + teenName (part)
        part = 0
    if part > 0 :
        name = name + " " +digitName(part)

    return name

def digitName(digit):
    if digit == 1 : return "one"
    if digit == 2 : return "two"
    if digit == 3 : return "three"
    if digit == 4 : return "four"
    if digit == 5 : return "five"
    if digit == 6 : return "six"
    if digit == 7 : return "seven"
    if digit == 8 : return "eight"
    if digit == 9 : return "nine"
    return ""
def tyName (number):
    if number >= 90 : return "ninety"
    if number >= 80 : return "eighty"
    if number >= 70 : return "seventy"
    if number >= 60 : return "sixty"
    if number >= 50 : return "fifty"
    if number >= 40 : return "fourty"
    if number >= 30 : return "thirty"
    if number >= 20 : return "twenty"
    return ""
def teenName(digit):
    if digit == 10 : return "ten"
    if digit == 11 : return "eleven"
    if digit == 12 : return "twelve"
    if digit == 13 : return "thirteen"
    if digit == 14 : return "fourteen"
    if digit == 15 : return "fifteen"
    if digit == 16 : return "sixteen"
    if digit == 17 : return "seventeen"
    if digit == 18 : return "eighteen"
    if digit == 19 : return "nineteen"
    return ""

main()