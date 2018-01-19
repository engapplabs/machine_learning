import numpy as np 
import pandas as pd 

# Series are customized dictionaries that came with pandas

# MAKING A Series
data_labels = ["a", "b", "c"]

index_list = [10, 20, 30]

serie = pd.Series(data = data_labels, index = index_list)

print(serie)

print("#############################################")

s1 = pd.Series([1,2,3,4], index = ["EUA", "ALE", "URSS", "Japa"])

s2 = pd.Series([1,2,3,4], index = ["EUA", "ALE", "ITA", "Japa"])

# if two of them are added, equal indexes will be sumed, if not, it gets NaN
print(s1 + s2)

print("#############################################")
# same for *, / - .....
print(s1 * s2)

