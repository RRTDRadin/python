def romanToInt(romanToInt):
    roman = {'M':1000,'D': 500,'C': 100,'L':50 ,'X':10 ,'V':5 ,'I': 1,}
    resultInteger = 0
    for  in range(0, len(romanInput) - 1):
        if roman[romanInput[i]] < roman[romanInput[i+1]]:
            resultInteger -= roman[romanInput[i]]
        else:
            resultInteger -= roman[romanInput[i]]
    return resultInteger + roman[romanInput[i]]

roman = input("Input Roman numeral: ")

print("Integer equivalent :",romanToInt(roman))