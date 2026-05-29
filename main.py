import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('network_logs.csv')

# Display first five rows
print(data.head())

# Show dataset information
print(data.info())

# Show statistical summary
print(data.describe())

# Check for missing values
print(data.isnull().sum())

# Remove rows with missing values
cleaned_data = data.dropna()
print(cleaned_data.info())