import numpy as np 
import pandas as pd 

# GOAL: GIVEN AN USER LIST FROM A DATABASE
# PREPARE A DATASET TO BE ANALYSED FOR A DATA SCIENTIST

# CREATING A CLASS TO HANDLE USER CLASS SCHEME
class User:

	def __init__(self, name, age, weight, height):
		self.name = name
		self.age = age
		self.weight = weight
		self.height = height

	def __str__(self):
		return "name: {}, age: {}, weight: {}, height: {}".format(self.name, self.age, self.weight, self.height)

# image we got this list from a data base
users = [User("Aurelio", 20, 69, 1.72),
		 User("Mario", 20, 70, 1.74),
		 User("Miranda", 20, 71, 1.70),
		 User("Rodrigo", 20, 75, 1.75)]

# we need to parse object atributes into an atributes matrix


# A FUNCTION TO PRINT USERS IN LIST
def print_users(users):
	for user in users:
		print(user, end = "")
	print("")

def users_to_atribute_matrix(users_list):
	''' This function gets an object list and parses it
		into an atribute matrix.

				Algorith
				--------
		1. Let states be a list of states
		2. for each user in users
			2.1. get current object scheme map
			2.2. get current values of map scheme state
			2.3. add to states list
		3. create a list with all elements in states
	'''
	states = []
	for user in users_list:
		instance_scheme = user.__dict__ # getting dictionary
		object_state = instance_scheme.values() # gettin state
		states.append(object_state) # adding state to list

	matrix_atributes = [list(object_state) for object_state in states]

	return matrix_atributes

# A List with atributes names
column_names = "name age weight height".split(" ")
indexes_list = list(range(0, len(users)))

# print(users_to_atribute_matrix(users))

user_data_frame = pd.DataFrame(data = users_to_atribute_matrix(users),
				 index = indexes_list, columns = column_names)
print(user_data_frame)


def build_data_frame_from_instance_list(instance_list):
	instance_atributes_map = instance_list[0].__dict__.keys() # getting atribute names
	column_names = list(instance_atributes_map) # putting atribute names in a list
	states = []
	for instance in instance_list:
		instance_atributes_map = instance.__dict__
		object_state = instance_atributes_map.values()
		states.append(object_state)

	indexes_list = list(range(len(instance_list)))

	atribute_matrix = [list(instance_state) for instance_state in states]

	return pd.DataFrame(data = atribute_matrix, index = indexes_list,
			columns = column_names)


print("###################################")

print(build_data_frame_from_instance_list(users))



