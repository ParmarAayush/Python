import pandas as pd
import numpy as np

ser = pd.Series()
print(ser)

data = np.array(['g','e','e','k','s'])
ser = pd.Series(data)
print(ser)

#import csv file
data = pd.read_csv("airlines.csv")
print(data)