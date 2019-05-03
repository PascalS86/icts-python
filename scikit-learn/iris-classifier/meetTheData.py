#Meet the data
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

irisDataset = load_iris()

#check data and how you can access it
print("Keys of irisDataset: {}".format(irisDataset.keys()))
print(irisDataset['DESCR'][:193] + "\n...")
print("Target names: {}".format(irisDataset.target_names))
print("Feature names: {}".format(irisDataset.feature_names))
print("Type of data: {}".format(type(irisDataset.data)))
print("Shape of data: {}".format(irisDataset.data.shape))
print("First five rows of data:\n{}".format(irisDataset.data[:5]))
print("Type of target: {}".format(type(irisDataset.target)))
print("Shape of target: {}".format(irisDataset.target.shape))
print("Target:\n{}".format(irisDataset.target))

X = irisDataset.data[:, :2]  # we only take the first two features.
y = irisDataset.target

xmin, xmax = X[:, 0].min() - .5, X[:, 0].max() + .5
ymin, ymax = X[:, 1].min() - .5, X[:, 1].max() + .5

plt.figure(2, figsize=(8, 6))
plt.clf()

# Plot the training points
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Set1,
            edgecolor='k')
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')

plt.xlim(xmin, xmax)
plt.ylim(ymin, ymax)
plt.xticks(())
plt.yticks(())

plt.show()
