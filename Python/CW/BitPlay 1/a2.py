def setOrNot(number, n):
    if number & (1 << (n - 1)):
        print( "\nSET")
    else:
        print("\nNOT SET")

number = int(input("Enter number: "))
n = int(input("Enter Bit number: "))
setOrNot(number, n)
