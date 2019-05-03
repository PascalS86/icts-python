import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split # for building test and training sets
from sklearn.neighbors import KNeighborsClassifier # for finding the k neighors based on featureset

irisDataset = load_iris()
xTrain, xTest, yTrain, yTest = train_test_split(irisDataset.data, irisDataset.target, random_state=0)

print("xTrain shape: {}".format(xTrain.shape))
print("yTrain shape: {}".format(yTrain.shape))

print("xTest shape: {}".format(xTest.shape))
print("yTest shape: {}".format(yTest.shape))


# create dataframe from data in xTrain
# label the columns using the strings in irisDataset.feature_names
irisDataframe = pd.DataFrame(xTrain, columns=irisDataset.feature_names)
# create a scatter matrix from the dataframe, color by yTrain
pd.plotting.scatter_matrix(irisDataframe, c=yTrain, figsize=(15, 15), marker='o', hist_kwds={'bins': 20}, s=60, alpha=.8)

#plt.show()

#build the model
knn = KNeighborsClassifier(n_neighbors=1) #we search for one neighbor
knn.fit(xTrain, yTrain) #this will train our model

#make a prediction
newArray = np.array([[5, 2.9, 1, 0.2]]) #measurments, to predict the species
prediction = knn.predict(newArray)
print("Prediction: {}".format(prediction))
print("Predicted target name: {}".format(irisDataset.target_names[prediction]))

#finally, we have to evaluate the model
yPred = knn.predict(xTest) #predict the values for your test set
print("Test set score: {:.2f}".format(np.mean(yPred == yTest))) #calc mean for your yPred based on your test set and your result
print("Test set score: {:.2f}".format(knn.score(xTest, yTest))) #calc the score for your test set
