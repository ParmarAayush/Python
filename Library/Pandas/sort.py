import pandas as pd 
import numpy as np

# data = np.random.rand(10,2) 
            # or
data_1D = (np.arange(20))
data = np.reshape(data_1D,(10,2))
columns = ['col2' ,'col1']

unsorted_df = pd.DataFrame(data=data, index=[1,4,6,2,3,5,9,8,8,7],columns=columns)
# print(unsorted_df)

sorted_df = unsorted_df.sort_index(ascending=False)
# print()
# print(sorted_df)

sorted_df = unsorted_df.sort_index(axis=1)
# print(sorted_df)

#Sorted By Value 
unsorted_df = pd.DataFrame({'col1': [2,1,1,1], 'col2': [1,3,2,4]}) 
print(unsorted_df)
print()
sorted_df = unsorted_df.sort_values (by='col1')
print(sorted_df)