import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Generate random data for demonstration
np.random.seed(42)
years = range(2010, 2021)
product_sales = np.random.randint(1000, 5000, size=len(years))

# Create a DataFrame
data = pd.DataFrame({'Year': years, 'Product_Sales': product_sales})

# Save data to a CSV file
csv_file_path = 'C:/Users/Rosha/OneDrive/Documents/Market research on new market entry/data_analysis/Product_Sales_Data.csv'
data.to_csv(csv_file_path, index=False)

# Create a line chart
plt.figure(figsize=(10, 6))
plt.plot(data['Year'], data['Product_Sales'], marker='o', color='b')
plt.xlabel('Year')
plt.ylabel('Product Sales')
plt.title('Health and Wellness Product Sales Over Time')
plt.grid(True)
plt.savefig('visualizations/line_chart_product_sales.png')
plt.show()

print("CSV file and line chart created successfully.")
