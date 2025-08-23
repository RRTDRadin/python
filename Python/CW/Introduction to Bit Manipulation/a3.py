def numberOfBits(n):
    count = 0

    while (n):
        count+= 1
        n>>=1

number = int(input("Ebter  your number: "))
print("Total bits :", numberOfBits(number))