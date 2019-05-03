import numpy as np
#create matrix
M = np.random.rand(3,3)
#create vector
v = np.random.rand(3)
#multply matrix with vector
mv = np.dot(M, v)
print(mv)
#solve systems of linear equations
v = np.linalg.solve(M, mv)
print(v)