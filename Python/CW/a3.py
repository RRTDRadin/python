file1 = open('CodingalUpdated.txt','w')

file2 = open ('CodingalUpdated.txt','w')

for line in file1.readline():
    if not (line.staryswith('Coding')):
        print(line)

file2.write(line)

file2.close()
file1.close()