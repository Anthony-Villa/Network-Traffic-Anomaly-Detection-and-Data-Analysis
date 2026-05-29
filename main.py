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

# Show top values in a column to vualize potential anomalies
print(cleaned_data['attack_detected'].value_counts())

# Create attack distribution chart
cleaned_data['attack_detected'].value_counts().plot(kind='bar')

plt.title('Attack Detection Distribution')
plt.xlabel('Attack Detected')
plt.ylabel('Count')
plt.show()