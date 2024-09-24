import pandas as pd
import numpy as np

data = ['Tom', 'William Rick', 'John', 'Alber@t', np.nan, '1234', 'SteveSmith']
s = pd.Series(data=data)
print(s)
print()
print(s.str.lower())
print(s.str.upper())