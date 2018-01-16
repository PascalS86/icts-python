import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split # for building test and training sets
from sklearn.neighbors import KNeighborsClassifier # for finding the k neighors based on featureset

# pass in column names for each CSV
u_cols = ['user_id', 'age', 'sex', 'occupation', 'zip_code']
users = pd.read_csv(os.path.join(os.path.dirname(__file__),'ml-100k/u.user'), sep='|', names=u_cols, encoding='latin-1')

r_cols = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
ratings = pd.read_csv(os.path.join(os.path.dirname(__file__),'ml-100k/u.data'), sep='\t', names=r_cols,
                      encoding='latin-1')

# the movies file contains columns indicating the movie's genres
m_cols = ['movie_id', 'title', 'release_date', 'video_release_date', 'imdb_url', 'unknown', 'Action', 'Adventure', 'Animation','Childrens', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi','Thriller', 'War', 'Western' ]
movies = pd.read_csv(os.path.join(os.path.dirname(__file__),'ml-100k/u.item'), sep='|', names=m_cols, usecols=range(len(m_cols)),
                     encoding='latin-1')

# create one merged DataFrame
movie_ratings = pd.merge(movies, ratings)
lens = pd.merge(movie_ratings, users)

# lets do an average rating for each movie
movie_stats = lens.groupby(['movie_id', 'unknown', 'Action', 'Adventure', 'Animation','Childrens', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi','Thriller', 'War', 'Western' ]).agg({'rating':np.mean}).reset_index()

# Now we build our training set
movie_ratings = lens[['movie_id', 'unknown', 'Action', 'Adventure', 'Animation','Childrens', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi','Thriller', 'War', 'Western', 'rating']]

y = movie_ratings.values[:, 0] # Target is the movie_id. First column of each row
X = movie_ratings.values[:, 1::] # rest are the values

xTrain, xTest, yTrain, yTest = train_test_split(X, y, test_size = 0.2, random_state=0)

print("xTrain shape: {}".format(xTrain.shape))
print("yTrain shape: {}".format(yTrain.shape))

print("xTest shape: {}".format(xTest.shape))
print("yTest shape: {}".format(yTest.shape))

#build the model
knn = KNeighborsClassifier(n_neighbors=3) #we search for one neighbor
knn.fit(xTrain, yTrain) #this will train our model

#finally, we have to evaluate the model
yPred = knn.predict(xTest) #predict the values for your test set
print("Test set score: {:.2f}".format(np.mean(yPred == yTest))) #calc mean for your yPred based on your test set and your result
print("Test set score: {:.2f}".format(knn.score(xTest, yTest))) #calc the score for your test set

#make a prediction
newArray = np.array([[0, 1, 1, 0,0, 1, 1, 0, 0,0, 0, 0, 0, 1, 0, 1,1, 0, 0, 5]]) #measurments, to predict the movie
prediction = knn.predict(newArray)
print("Prediction: {}".format(prediction))

print("Predicted target name: {}".format(movies.loc[movies['movie_id'] == prediction[0]]))
