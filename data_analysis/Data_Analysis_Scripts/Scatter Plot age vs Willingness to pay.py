import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV file
csv_file_path = 'C:/Users/Rosha/OneDrive/Documents/Market research on new market entry/data_analysis/CSV Files/Product_Preference 2.csv'
data = pd.read_csv(csv_file_path)

# Display the first few rows of the DataFrame
print(data.head())

# Basic analysis
average_age = data['Age'].mean()
natural_preference_count = data['Natural_Ingredients_Preference'].sum()
willingness_to_pay_count = data['Willingness_To_Pay'].sum()

print(f"Average Age: {average_age:.2f}")
print(f"Number of respondents preferring natural ingredients: {natural_preference_count}")
print(f"Number of respondents willing to pay for personalized solutions: {willingness_to_pay_count}")

# Data visualization: Scatter Plot
plt.figure(figsize=(10, 6))
plt.scatter(data['Age'], data['Willingness_To_Pay'], color='blue', alpha=0.7)
plt.xlabel('Age')
plt.ylabel('Willingness to Pay')
plt.title('Scatter Plot: Age vs. Willingness to Pay')
plt.savefig('visualizations/scatter_plot.png')
plt.show()
