number= int(input("Enter your number: "))

origional_number = number
reversed_number =0
 
while number > 0:
    digit= number % 10
    reversed_number = reversed_number * 10 + digit
    number //= 10

if origional_number  == reversed_number:
    print(origional_number," is an palindrome")
else:
    print(origional_number," is not an palindrome")
