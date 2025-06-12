my_set = {1,2,2,3,4,4,4}
print("Set :", my_set)

my_set.add(5)
print("Updated Set: ", my_set)

setx={"green","pink"}
sety=("pink","yellow")
print("Origonal set:\n",sety)
      
print("\n Intersection of setx & sety: ")

print("\n union of setx set y: ")

setu=setx.union(sety)
print(setu)

print

print("\n difference of 2 sets: ")

set_x=setx.difference(sety)
set_y=sety.difference(setx)

print(set_x)
print(set_y)

print("\n symettric difference: ")
set_sd=setx.symetric_difference(sety)
print(set_sd)