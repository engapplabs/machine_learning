from keras.models import Sequential
from keras.layers import Dense
import numpy as np

'''
sleept studied -> score
	8 	3           7
	10	4			8
	10	5			9.5
	5	7			4.5
	10	6			10

max_value = 10, to normalize
'''

x = np.array([[8.0, 3.0], [10.0, 4.0], [10.0, 5.0], [5.0, 7.0], [5.0, 10.0],[10.0, 6.0]])
y = np.array([[7.0], [8.0], [9.5], [4.5], [5.0],[10.0]])

model = Sequential()

model.add(Dense(5, input_dim = 2))
model.add(Dense(1))

model.compile(optimizer = 'sgd', loss = 'mse', metrics = ['acc'])

model.fit(x, y, epochs = 3000)

while True:
	sleept = input("Sleept: ")
	studied = input("Studies: ")

	data_list = [float(sleept), float(studied)]

	t = np.asmatrix(data_list)

	result = model.predict(t)

	print("Previsto: " + str(2))
