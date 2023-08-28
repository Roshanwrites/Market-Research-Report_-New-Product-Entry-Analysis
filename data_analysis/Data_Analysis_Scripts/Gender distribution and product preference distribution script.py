import pandas as pd
import matplotlib.pyplot as plt

# Load survey data from CSV file
csv_file_path = 'C:/Users/Rosha/OneDrive/Documents/Market research on new market entry/data_analysis/Product_Preference.csv'
survey_data = pd.read_csv(csv_file_path)

# Bar chart: Gender Distribution
gender_counts = survey_data['Gender'].value_counts()
plt.figure(figsize=(6, 4))
plt.bar(gender_counts.index, gender_counts.values, color='skyblue')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.title('Gender Distribution')
plt.show()

# Pie chart: Product Preference Distribution
product_preference_counts = survey_data['Product_Preference'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(product_preference_counts.values, labels=product_preference_counts.index, autopct='%1.1f%%', colors=['lightblue', 'lightgreen', 'lightcoral'])
plt.title('Product Preference Distribution')
plt.axis('equal')  # Equal aspect ratio ensures that the pie is drawn as a circle.
plt.show()

