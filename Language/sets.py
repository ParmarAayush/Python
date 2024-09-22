s1 = {2,3,4,3}
s2 = {4,5,6,7,8}
print(s1)
print(s1.union(s2)) # s1 value update with union of s1 and s2
print(s1)
s1.update(s2)
print(s1)
s3 = {2}
print(s1.intersection(s3))
print(s1.intersection_update(s3))
print(s1)

# s1.remove("100") ## Generate Error 
s1.discard("100") ## not generate error 

#pop is use for remove last element 
#del entire set "del set_name" and clear is remove all elements 