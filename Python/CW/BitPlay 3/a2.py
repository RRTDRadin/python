def diviide(ourDividend, ourDivisor):
    sign = (-1 if((ourDividend < 0) ^
                  (ourDivisor < 0 )) else 1);
    ourDivisor = abs(ourDivisor);
    ourDividend = abs(ourDividend);

    quotientNumber = 0
    tempNumber = 0

    for  i in range(31, -1, -1):
        if sign ==-1:
            quotientNumber=-quotientNumber
            return quotientNumber 
        
a = int(input("Enter  a for a/b: "))
        
b = int(input("Enter  b for a/b: "))
print("Result of ",a,"/",b," is ",diviide(a, b))
    