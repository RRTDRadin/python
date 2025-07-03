file = open('Codingal.txt', 'r')
print(file.read())
file.close()

file = open('Codingal.txt', 'r')
print("\n Read in parts \n")
print(file.read(8))
file.close()

file = open('Codingal.txt', 'a')
print("Hi! I am Penguin and I am 1 uears old")
file.close()