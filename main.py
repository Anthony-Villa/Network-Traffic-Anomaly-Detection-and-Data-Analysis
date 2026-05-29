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