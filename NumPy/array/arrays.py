#import the numpy package
import numpy as np

#create a vector
vec = np.array([0, 1, 1.5, 2.75])
print (vec)

#create a linear vector
vec2 = np.arange(10)
print(vec2)

#create another linear vector
vec3 = np.arange(1, 10, 0.5) # arange([start,] stop, [step,] dtype=None)
print(vec3)

#Create a vector with zeros
zeroVector = np.zeros(4)
print(zeroVector)

#create a matrix
matrix = np.array([[3, 5, 2, 4],
       [7, 6, 8, 8],
       [1, 6, 7, 7]])

print(matrix)