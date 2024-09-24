import numpy as np

a = np.array([[1,3],[1,2]])
b = np.array([[1,2],[1,5]])

print(a + b)

#Structured arrays
x = np.array([('Rex', 9, 81.0), ('Fido', 3, 27.0)],dtype=[('name', 'U10'), ('age', 'i4'), ('weight', 'f4')])
print(x)