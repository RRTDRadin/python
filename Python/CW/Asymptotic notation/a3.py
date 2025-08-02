def OnSquareTime(n):
    iteration=0
    for i in range(1,n):
        for j in range(1,n):
            print("*", end =" ")
            iteration+=1
        print("")
    print("When n is ",n," Iterations = ", iteration)

OnSquareTime(5)
OnSquareTime(4)
OnSquareTime(3)

print("\nWith every 'n' the time taken equals n^2")
print("O(n^2)")