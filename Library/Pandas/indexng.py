import pandas as pd

data = pd.read_csv("nba.csv", index_col ="Name")
first = data["Age"]
# print(first)

# retrieving row by loc method
first = data.loc["Avery Bradley"]
second = data.loc["R.J. Hunter"]

# print(first, "\n\n\n", second)

# retrieving rows by iloc method
row2 = data.iloc[3]