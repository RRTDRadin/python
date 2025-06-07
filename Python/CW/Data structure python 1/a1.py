Fruit = ['Apple', 'Grabe', 'Mango', 'Banana', 'Kiwi']

print("Length of list: ", len(Fruit))
print("First Element: ", Fruit[0])
print("Last Element: ", Fruit[-1])


Fruit.append('Papaya')
print("Updated List: ", list)

Fruit.remove('Grabe')
print("Updated List: ", list)

Fruit.sort()
print("Sorted List: ", list)

Fruit.pop(1)
print("Updated List: ", list)

Fruit.reverse()
print("Reversed List: ", list)

print("Multiplication on list: ", Fruit)

Fruit = Fruit[:4]
print("Sliced List: ", list)

Fruit.clear()
print("Updated List: ", list)