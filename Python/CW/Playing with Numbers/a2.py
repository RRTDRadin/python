numberlarge = int(input("Enter the larger number: "))
numbersmall = int(input("Enter the smaller number: "))

while(numbersmall):
    numberStore = numbersmall
    numbersmall = numberlarge % numbersmall
    numberlarge = numberStore

print("HCF is: ",numberlarge)