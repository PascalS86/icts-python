import numpy as np
import matplotlib.pyplot as plt # neccessary for plotting the image
from scipy import misc # neccessary for loading the image

f = misc.face() # loads an image of a racoon

print(type(f)) #type of ndarray

print(f) #print the array
print(f.shape) #print the shape

f = f[::-1, ::-1, ::-1] #solution with indexing

#f = np.flipud(f)

plt.imshow(f) #load image for plot
plt.show() #show plot of image
