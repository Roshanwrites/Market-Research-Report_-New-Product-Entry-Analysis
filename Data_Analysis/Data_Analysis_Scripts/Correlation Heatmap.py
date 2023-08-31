import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample dataset with attributes
data = {
    'Age': [25, 30, 35, 40, 45, 50, 55, 60, 65, 70],
    'Income': [50000, 60000, 75000, 80000, 90000, 95000, 100000, 105000, 110000, 120000],
    'Spending': [100, 120, 150, 160, 180, 190, 200, 210, 220, 240],
    'Satisfaction': [8, 7, 9, 8, 9, 9, 10, 8, 7, 9]
}

df = pd.DataFrame(data)

# Calculate correlation matrix
correlation_matrix = df.corr()

# Create a correlation heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0, fmt=".2f")

plt.title('Correlation Heatmap')
plt.show()
