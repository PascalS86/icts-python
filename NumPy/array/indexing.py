import numpy as np

#create a Vector with 10 members
vec = np.arange(10)

#get the first element
first = vec[0]
print(first)
#get the last element
last = vec[-1]
print(last)
#create matrix
matrix = np.array([[3, 5, 2, 4],
       [7, 6, 8, 8],
       [1, 6, 7, 7]])

#get element from matrix
lastRowFirstColumn = matrix[2,0]
print(lastRowFirstColumn)

#Slicing
#get first five elements of vec
firstFive = vec[:5]
print(firstFive)

#get last five elements of vec
lastFive = vec[5:]
print(lastFive)

#get middle elements of vec
middle = vec[2:6]
print(middle)

#get every even element
even = vec[::2]
print(even)

#get vector invers
print(vec[::-1])