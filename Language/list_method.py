l1 = [i for i in range(5)]
print(l1)
l1.append(5)
l1.insert(6,599)
print(l1)

l2 = l1 # l2 refrese to l1
l2[0] = 12
print(l1) # i change in l2 but it refelect on l1 also, l2 = l1 now l2 refres to l1

l3 = l1.copy()
l3[0] = 124
print(l1) # not change 
print(l3) # change 

m = [100,200,300]
l1.extend(m)
print(l1) # same thing using m + l1