import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0.1, 10, 0.1)
y = np.sin(x)

print(y)
print(x)

plt.figure(figsize=(10,8))
plt.plot(x,y)
plt.show()