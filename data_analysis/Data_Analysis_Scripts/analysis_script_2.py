import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load survey data from CSV file
csv_file_path = 'C:/Users/Rosha/OneDrive/Documents/Market research on new market entry/data_analysis/survey_data.csv - Sheet1.csv'
survey_data = pd.read_csv(csv_file_path)

# Calculate average age
average_age = survey_data['Age'].mean()
print(f"Average Age: {average_age:.2f} years")

# Generate a box plot of ages
plt.figure(figsize=(8, 6))
sns.boxplot(x=survey_data['Age'])
plt.xlabel('Age')
plt.title('Age Distribution')
plt.show()

# Calculate percentage preferring natural ingredients
natural_ingredients_preference = (survey_data['Natural_Ingredients_Preference'].sum() / len(survey_data)) * 100

# Calculate percentage willing to pay for personalized solutions
willingness_to_pay = (survey_data['Willingness_To_Pay'].sum() / len(survey_data)) * 100

# Print analysis results
print(f"Percentage preferring natural ingredients: {natural_ingredients_preference:.2f}%")
print(f"Percentage willing to pay for personalized solutions: {willingness_to_pay:.2f}%")

# Exclude non-numeric columns from correlation analysis
numeric_columns = survey_data.select_dtypes(include=['number'])
correlation_matrix = numeric_columns.corr()

# Print correlation matrix
print("\nCorrelation Matrix:")
print(correlation_matrix)

# Generate a heatmap of correlations
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
plt.title('Correlation Heatmap')
plt.show()
