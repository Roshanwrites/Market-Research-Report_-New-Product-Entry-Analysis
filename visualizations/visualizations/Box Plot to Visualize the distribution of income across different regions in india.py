import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample dataset with regions and income
data = {
    'Region': ['North', 'South', 'East', 'West', 'Central', 'North', 'South', 'East', 'West', 'Central'],
    'Income': [50000, 60000, 75000, 80000, 90000, 95000, 100000, 105000, 110000, 120000]
}

df = pd.DataFrame(data)

# Create a box plot
plt.figure(figsize=(8, 6))
sns.boxplot(x='Region', y='Income', data=df, palette='Set3')

plt.title('Distribution of Income across Regions')
plt.show()
