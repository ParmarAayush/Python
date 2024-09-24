l = [i for i in range(1,6)]
def cube(x):
    return x * x * x

# Method 1 Normal method
newl = []
for item in l:
    newl.append(cube(item))

print(f"{l} = > {newl}")

# Method 2 using map
cubeList = list(map(cube, l))
print(f"Same output is => {cubeList}")

#filter
def filterFunction(x):
    return x > 4

filterList = list(filter(filterFunction, l))
print(f"filter output => {filterList}")


#Reduce : operate on two 

from functools import reduce

sum = reduce(lambda x, y: x + y, l)

print(sum)