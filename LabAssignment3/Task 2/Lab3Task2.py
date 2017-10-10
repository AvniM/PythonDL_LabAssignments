# ---------------------------------------------------------------------
#   Lab Assignment 3 - Task 2
#   For customer dataset, implement K-means clustering with 5 clusters
#   Avni Mehta, Class Id: 15
# ---------------------------------------------------------------------

# Importing Libraries
from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt


# Read text from file into array
def read_data(filename):
    dataset = pd.read_csv(filename)
    # Col 4 is for annual income
    # Col 5 is for spending score
    return dataset.iloc[:, [3, 4]].values


# k-means for n clusters
def apply_kmeans(data, n):
    # Fit k-means for given data
    kmeans = KMeans(n_clusters=n, init='k-means++', random_state=10)
    y = kmeans.fit_predict(data)
    return kmeans, y


# Plot the graph
def plot_graph(X, y, k):
    # Plotting clusters
    plt.scatter(X[y == 0, 0], X[y == 0, 1], s=80, c='cyan', label='Cluster 1')
    plt.scatter(X[y == 1, 0], X[y == 1, 1], s=80, c='red', label='Cluster 2')
    plt.scatter(X[y == 2, 0], X[y == 2, 1], s=80, c='magenta', label='Cluster 3')
    plt.scatter(X[y == 3, 0], X[y == 3, 1], s=80, c='green', label='Cluster 4')
    plt.scatter(X[y == 4, 0], X[y == 4, 1], s=80, c='blue', label='Cluster 5')
    # Plotting centroids
    plt.scatter(k.cluster_centers_[:, 0], k.cluster_centers_[:, 1], s=200, c='yellow', label='Centroids')
    # Setting labels
    plt.title('Clusters of Customers')
    plt.xlabel('Annual Income (k$)')
    plt.ylabel('Spending Score (1-100)')
    # Legend to show the label for each cluster
    plt.legend()
    # Show the plot
    plt.show()


# Main Activity
print("\n----------------------------------------------------------------")
print("K-means Clustering for Customers dataset")
print("----------------------------------------------------------------")

# Read Customer dataset
# Clustering is based on fields - annual income and spending score
print(" 1. Reading Customers dataset..")
customer = read_data('Customers.csv')

# Apply K-means to dataset for 5 clusters
no_of_clusters = 5
print(" 2. Applying kmeans clustering for " + str(no_of_clusters) + " clusters..")
k_means, y_pred = apply_kmeans(customer, no_of_clusters)

# Plot the graph
print(" 3. Plotting the graph..")
plot_graph(customer, y_pred, k_means)