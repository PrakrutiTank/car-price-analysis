# Toyota Corolla Data Analysis and k-NN Implementation

## Description
This project performs exploratory data analysis (EDA) and applies the k-Nearest Neighbors (k-NN) algorithm on the Toyota Corolla dataset. The analysis includes data cleaning, statistical summaries, and visualization, followed by a k-NN model for price prediction.

## Requirements
Ensure you have the following Python libraries installed before running the code:
- `numpy`
- `pandas`
- `matplotlib`
- `sklearn`

Install them using:
```bash
pip install numpy pandas matplotlib scikit-learn
```

## Dataset
The dataset used is `ToyotaCorolla1[1].csv`, which contains information about Toyota Corolla cars. The data includes numerical and categorical attributes, such as price, age, fuel type, and manufacturing details etc.

## Steps Performed

### 1. Exploratory Data Analysis (EDA)
- Load the dataset using `pandas.read_csv()`.
- Display shape and missing values.
- Count unique values in each column.
- Extract numerical data and compute statistics like sum, mean, median, variance, and standard deviation.
- Plot distributions for various features:
  - Price vs. Index
  - Price vs. Age
  - Manufacturing Month distribution (bar chart)
  - Fuel Type and Color distributions (pie charts)

### 2. k-Nearest Neighbors (k-NN) Implementation
- Select important features for training.
- Split the dataset into training and testing sets using `train_test_split()`.
- Implement the Euclidean distance function.
- Implement the k-NN algorithm:
  - Compute distances between test points and training points.
  - Select k nearest neighbors.
  - Predict the target variable using the mean of neighbor values.

### 3. Model Evaluation
- Calculate error metrics:
  - Mean Absolute Error (MAE)
  - Mean Squared Error (MSE)
  - Root Mean Squared Error (RMSE)
  - Mean Absolute Percentage Error (MAPE)

## Results
The script provides insights into the Toyota Corolla dataset and predicts prices using the k-NN model. Visualizations help in understanding data distribution and relationships between features.

## Author
Prakruti Tank
Vasava Jignal
