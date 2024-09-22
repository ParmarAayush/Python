## is compare location in memory and equals to compare value
a = 2
b = 2

print(f"address of a is {id(a)} and value is {a}")
print(f"address of b is {id(b)} and value is {b}")
print(a is b," ", a == b)

a = [1,2,3]
b = [1,2,3]

print(f"address of a is {id(a)} and value is {a}")
print(f"address of b is {id(b)} and value is {b}")
print(f"Based on location {a is b} and Based on value {a == b}")

