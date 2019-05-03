import numpy as np

#create vector
vec = np.arange(9)

#reshape vector in 3x3 matrix
matrix = vec.reshape((3,3))
print(matrix)

#copy matrix
matrix2 = matrix.copy()
#change first column, first entry of matrix2
matrix2[:, 0][0] = 9
print(matrix)
print(matrix2)

#some sample for concatenate, vstack/hstack and split (vsplit, hsplit)
#those methods can also be found on numpy.org -> manual

#copy first column as new vector
vec2 = matrix[:, 0].copy()
print(vec2)

#concatenate on axis 0
print(np.concatenate([vec, vec2], axis=0))

#concatenate maxtrix and matrix2 on axis=1
print(np.concatenate([matrix, matrix2], axis=1))

# horizontally stack the arrays
y = np.array([[99],
              [99],
              [99]])
print(np.hstack([matrix, y]))

#finally we split the vector
x1, x2 = np.split(vec, [3])
print(x1)
print(x2)

#and the matrix
y1, y2 = np.vsplit(matrix, [2])
print(y1)
print(y2)