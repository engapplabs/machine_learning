import numpy as np 
import pandas as pd

# it mean that all random numbers are equals in any pc
np.random.seed(1)

#  CREATING A DATA FRAME
''' 
=> made of: list of instances and a list of names for each atribute in instances

'''
random_serie = np.random.randn(5, 4) # matrix 5 x 4 from a normal distribuition

indexes = "A B C D E".split(" ") # indexes list

column_names = "W X Y Z".split(" ") # column names
 
df = pd.DataFrame(data = random_serie, index = indexes, columns = column_names)

print("		Data frame")
print(df)

print("############################################")

# filtering data from a column name (atribute)
print("		atribute names")
print(df["W"])	# it gets a Serie

print("############################################")

## getting a list of columns (atributes)
print("		atributes list")
print(df[["W", "Z"]])

print("############################################")

# adding new columns to data frame
df["new"] = df["W"] + df["X"]
print("		data frame with new columns")
print(df)

print("############################################")

# deleting a column
df = df.drop("new", axis = 1)
# or df.drop("new", axis = 1, inplace = True)
print("		deleted columns")
print(df)

print("############################################")

# "hashing on dataframes"
print("		Doing hashing")
print(df.loc["A", "W"])

print("############################################")

# make a select in a data frame
print("		selected area of data frame")
# getting instances A, B and its atributes x, y and z
print(df.loc[["A", "B"], ["X", "Y", "Z"]])

print("############################################")

# hashing with indexes (numbers)
print("		Using iloc to hash")
print(df.iloc[1:4, 2:])


