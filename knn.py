import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

# Load data
data = pd.read_csv(r"C:\Users\hp\Downloads\ToyotaCorolla1[1].csv", header='infer')

# Selecting features and target variable
ind = [3, 4, 5, 6, 9, 16, 17]
X = data.iloc[:, ind]
y = data.iloc[:, 2]

# Splitting dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Euclidean distance function
def eulidean_distance(xy_train, xy_test):
    return np.sqrt(np.sum((xy_train - xy_test) ** 2, axis=1))

# k-NN function
def knn(x_train, x_test, k):
    distances = np.array([eulidean_distance(x_train, test_point) for test_point in x_test.to_numpy()])
    sorted_indices = np.argsort(distances, axis=1)[:, :k]  # Get indices of k nearest neighbors
    return sorted_indices

# Get k value
k = int(input("Enter k: "))  

# Compute k-nearest neighbors
nearest_neighbors = knn(X_train, X_test, k)
y_pred_list = []

# Predicting target values
for neighbors in nearest_neighbors:
    y_pred = np.mean(y_train.iloc[neighbors])  # Get y_train values using indices
    y_pred_list.append(y_pred)

# Convert predictions to numpy array
y_pred = np.array(y_pred_list)

# Error calculations
mae = np.mean(np.abs(y_test.to_numpy() - y_pred))
mse = np.mean((y_test.to_numpy() - y_pred) ** 2)
rmse = np.sqrt(mse)

mape_a = np.abs(y_test.to_numpy() - y_pred)
mape_b = np.where(y_test.to_numpy() != 0, mape_a / y_test.to_numpy(), 0)
mape = np.mean(mape_b)

# Print errors
print("Mean Absolute Error:", mae)
print("Mean Squared Error:", mse)
print("Root Mean Squared Error:", rmse)
print("Mean Absolute Percentage Error:", mape)
