import pandas as pd
import random

data = {
    "Maths" : [random.randint(0,100) for _ in range(5)],
    "Science" : [random.randint(0,100) for _ in range(5)],
    "English" : [random.randint(0,100) for _ in range(5)],
    
}

print(data)
df = pd.DataFrame(data=data)
print(f"Data Frame is \n {df}")
print(f"Sum is \n {df.sum()}")