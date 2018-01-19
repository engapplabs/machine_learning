import numpy as np

# python default list
simple_list = [1,2,3]

# numpy array
np_array = np.array(simple_list)
print(np_array)

# with matrix
np_matrix = np.array([[1,2], [3,4]])
print(np_matrix)

# arange - similar to range
np_range = np.arange(0, 10) # from 0 til 9
print(np_range)

# matrix only with zeros
np_zeros = np.zeros(3) # -array
print(np_zeros)

np_zeros_matrix = np.zeros((3,3)) #- matrix
print(np_zeros_matrix)

# identity matrix
np_identity = np.eye(4)
print(np_identity)

# linspace : start, end, how many numbers equaly spaced in between
s1 = np.linspace(0, 10, 2) # from 0 til 9 with only 2 numbers
print(s1)

s2 = np.linspace(0, 10, 3) # from 0 til 9 with only 3 numbers
print(s2)


############## np.random ###############
# it creates random numbers according with some rule

##>>>>>>> np.random.rand(): 
	# will create numbers from 0 till 1 using uniform distribuition
	# all these numbers are following a uniform distribuition
	# equal probalilty to be selected

s3 = np.random.rand(5) # give five random
print(s3)

s4 = np.random.rand(5) * 100 # from 0 till 99.99
print(s4)
	
	# for matrix
m1 = np.random.rand(2, 2) # random matrix
print(m1) 

##>>>>>>>> np.random.randn
	# return random numbers that don't came from a normal distribuition (gaussian)

s5 = np.random.randn(4)	
print(s5)

##>>>>>> rp.random.randint : show int numbers
random_ints = np.random.randint(0, 100, 10) # get 10 number from range 0-99
print(random_ints)

############## reshape ###################

# current shape of v1 is an 1d array
v1 = np.random.rand(25)
print(v1)

# reshape to 5 x 5 d
v2 = v1.reshape((5,5))
print(v2)

# get shape of a vector
print(v2.shape)

# get max value
print(v2.max())

# get max value index
print(v2.argmax())

# get min value
print(v2.min())

# get min value index
print(v2.argmin())

print("---------------------------------------------------------")

array = np.arange(0, 30, 3)
print(array)

# getting values
print(array[4])

# gettin sublist
print(array[2:5]) # from 2 till 4

print(array[:4]) # from 0 till 3

array[2] = 100
print(array)


# create an array of 50 elements and reshape it to a matrix 5x10
a2d = np.arange(50).reshape(5, 10)
print(a2d)

print(a2d.shape)

print(a2d[:3][:]) # line 0, 1 and two complete

v2d = a2d[:] # they're sharing same pointer
v2d = a2d[:].copy() # now they're different

v2d[0][0] = -505
print(v2d == a2d)


print(a2d[1:4, 5:]) # it gives lines 1, 2 and 3 and lines from 5 till end


# checking conditionals
print(a2d > 50)


print("-------------------------------------------------------------")

a = np.arange(0, 16)

# sum two arrays
print(a + a)

# mult
print(a * a)


# get sqrt of elements
print(np.sqrt(a))

# get mean
print(np.mean(a))

# get standard deviation
print(np.std(a))










