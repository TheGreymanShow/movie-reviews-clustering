#Step 1: Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Step 2: Importing the dataset
dataset = pd.read_csv('D:/Projects/Movie Reviews Clustering/Datasets/final.csv')

#Step 3: Cleaning
# checking for missing values
dataset.isnull().any()
# if any missing values found, fill them using "Fill Values Forward" method
dataset = dataset.fillna(method='ffill')
# Limiting Floating values to 2 decimal places (for uniformity)
for index,row in dataset.iterrows():
    x=row['Avg Rating']
    x=float("{0:.2f}".format(x))    
    dataset.loc[index,'Avg Rating']=x
    dataset.loc[index,'Y']=4.0
    
X = dataset.iloc[:, [8,10]].values
    
#Step 4: Using the elbow method to find the optimal number of clusters
from sklearn.cluster import KMeans
wcss = []
for i in range(1, 11):
    # Used K-Means++ for better random centroid initialization
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

'''
plt.plot(range(1, 11), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()'''

# From the Graph, I the elbow appears around the number 3
# Hence, I will be considering 3 clusters

#Step 5: Fitting K-Means to the reviews dataset
kmeans = KMeans(n_clusters = 3, init = 'k-means++', random_state = 0)
y_kmeans = kmeans.fit_predict(X)

#Step 6: Visualizaing the clusters using Scatter Plots
a=X[y_kmeans == 0]
b=X[y_kmeans == 2]
c=X[y_kmeans == 1]

plt.scatter(a[:,0],a[:,1],s=10,c = 'red', label = 'Cluster 1')
plt.scatter(b[:,0],b[:,1], s=10,c = 'blue', label = 'Cluster 2')
plt.scatter(c[:,0],c[:,1], s=10,c = 'green', label = 'Cluster 3')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 150, c = 'orange', label = 'Centroids')
plt.xticks(np.arange(1,5.5,0.5))
plt.yticks(np.arange(10), ('0','1', '2', '3', '4', '5','6','7','8','9'))
plt.title('Clusters of movies')
plt.xlabel('Average Ratings')
plt.ylabel('Dummy Variable')
plt.legend()
plt.show()

dataset.to_csv('D:/Projects/Movie Reviews Clustering/Datasets/final.csv')

