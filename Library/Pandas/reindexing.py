import pandas as pd
data = {"P":[4, 7, 1, 8, 9], 
        "Q":[6, 8, 10, 15, 11], 
        "R":[17, 13, 12, 16, 14], 
        "S":[15, 19, 7, 21, 9]}

index =["Parker", "William", "Smith", "Terry", "Phill"]

info = pd.DataFrame(data,index)
print(info)

new_index = ["Aayush", "Aniket", "Raj", "Dixant", "Jay"]
print(info.reindex(new_index)) # not change orignal dataFram return new data frame 

print(info.reindex(new_index,fill_value=100))

# How to fill old values 