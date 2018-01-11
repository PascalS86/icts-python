import numpy as np

#create random array
a = np.random.rand(100)

print("Mean height:       ", a.mean())
print("Standard deviation:", a.std())
print("Minimum height:    ", a.min())
print("Maximum height:    ", a.max())

print("25th percentile:   ", np.percentile(a, 25))
print("Median:            ", np.median(a))
print("75th percentile:   ", np.percentile(a, 75))