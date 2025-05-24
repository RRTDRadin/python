num = int(input("Enter number to check : "))

if num>50:
    print("Number isgreater than 50")
    if num%2==0:
        print("And the number is even.")

    else:
        print("And it is odd.")

else:
    print("Number is less than 50")