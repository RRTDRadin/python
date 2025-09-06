def checkIfSame(number1, number2):
    if((number1 ^ number2) != 0):
        print("Number is not equal")
    else:
        print("Bothe numbers are equal")
number1 = int(input("Enetr first number to compare: "))
number2 = int(input("Enetr second number to compare: "))

checkIfSame(number1, number2)