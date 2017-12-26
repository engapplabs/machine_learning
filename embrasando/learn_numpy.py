# importing
import numpy as np

# creating an array of 6 elements
a = np.array([0, 1, 2, 3, 4, 5])
print(a)

# dimentions of array
print("Dimension: {}".format(a.ndim))

# getshape
print(a.shape)

# gettin an array redimensioning array a
b = a.reshape(3, 2) 
# a has 6 elements, here we reshape it into  2 dimentions and scalar product is 6
print(b)

print("Dimensions now: {}, shape: {}".format(b.ndim, b.shape))

# getting copy of arrays
c = a.reshape(3,2).copy()
print(c)

# changing value of a index
c[0][0] = -505

# printing to test c and a
print(c)
print(a)

# multiplying elements for a value
print(a * 2)

# aplying checking into an array
print(a > 2)

# HANDLING NON EXISTING VALUES
# supose we have
c = np.array([1,2, np.NAN, 3,4])
print(c)
# remove non-numbers
d = c[~np.isnan(c)]
print(d)
