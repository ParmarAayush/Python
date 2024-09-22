l1 = [i for i in range(41,51)]
print(l1)

count = 0
for i in l1:
    print(i, end=" ")
    count = count + 1
print(f"\nValue of count is {count}")

# above same thing is done by enumrate but in easy way

for index, i in enumerate(l1, start=1):
    print(f"at index {index} value {i}")

# start value of enumare with 1 by passing start=1 else default is zero