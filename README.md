# car-price-analysis
Using python
# **Toyota Corolla Car Dataset Analysis**
## **Project Overview**
This project analyzes the **Toyota Corolla** car dataset to explore various attributes like price, age, fuel type, manufacturing month, and color. The goal is to perform **data cleaning, statistical analysis, and visualization** to understand trends and distributions within the dataset.

## **Dataset**
- The dataset contains information about Toyota Corolla cars, including numerical and categorical features.
- The data is loaded from a CSV file.

## **Requirements**
The following Python libraries are required:
```python
import numpy as np  
import pandas as pd  
import math  
import matplotlib.pyplot as plt  
```

Install missing dependencies using:

```bash
pip install numpy pandas matplotlib  
```

## **Project Workflow**

### **1. Data Loading & Cleaning**
- Read the dataset using `pandas`.
- Check for missing values.
- Identify unique values in each column.

### **2. Data Exploration & Summary Statistics**
- Extract numerical and categorical data.
- Compute statistical measures such as sum, mean, median, standard deviation, variance, and range.
- Identify unique values and mode for categorical columns.

### **3. Data Visualization**
- **Scatter Plots** to show relationships between price and other numerical attributes.
- **Bar Charts** to display the distribution of manufacturing months.
- **Pie Charts** to show the proportions of fuel types and car colors.

## **Visualizations Included**
📌 **Index vs. Price** (scatter plot)\
📌 **Age vs. Price** (scatter plot)\
📌 **Manufacturing Month Distribution** (bar chart)\
📌 **Fuel Type Distribution** (pie chart)\
📌 **Color Distribution** (pie chart)

## **Key Insights**
- The price of cars varies significantly with age and other factors.
- Certain fuel types and colors are more common.
- Manufacturing month distribution shows trends in car production.

## **Usage**

Run the script in a Python environment:
```bash
python analysis_script.py  
```
Modify the CSV file path if needed.

## **Conclusion**

This project provides valuable insights into used car pricing, helping buyers and sellers make informed decisions. 🚗📊

