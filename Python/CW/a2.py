file = open('Codingal.txt', 'r')
print("Read First line...")
print(file.readline())
file.close()

file = open('Codingal.txt', 'r')
print("Reading multiple lines...")
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

file = open('Codingal.txt', 'r')
print("Looping through the lines...")
for line in file:
    print(line)
file.close()