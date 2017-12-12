import tensorflow as tf 

input1 = tf.placeholder("float", name = "input1")

input2 = tf.placeholder("float", name = "input2")

x = tf.Variable(dtype = "float")

output = tf.Variable(dtype = "float")

x = input1 * input2

output = x * x
