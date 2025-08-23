def SieveOfEratosthenes(num):
    prime = [True for i in range(num+1)]   # Step 1: Assume all numbers are prime
    p = 2                                  # Step 2: Start with the first prime number

    while (p * p <= num):                  # Step 3: Check numbers till sqrt(num)
        if (prime[p] == True):             # Step 4: If 'p' is still prime
            for i in range(p * p, num+1, p):  # Step 5: Mark multiples of 'p' as not prime
                prime[i] = False
        p += 1

    # Step 6: Print all prime numbers
    for p in range(2, num+1):
        if prime[p]:
            print(p)
