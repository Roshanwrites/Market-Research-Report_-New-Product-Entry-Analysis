import pandas as pd
import matplotlib.pyplot as plt

# Load survey data from CSV file
survey_data = pd.read_csv('survey_data.csv')  # Replace with your file path

# Descriptive statistics
print("Descriptive Statistics:")
print(survey_data.describe())

# Data visualization
plt.figure(figsize=(10, 6))
plt.hist(survey_data['Age'], bins=10, color='blue', alpha=0.7)
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Distribution of Participant Ages')
plt.show()

# Calculate preferences for natural ingredients
natural_ingredients_preference = (survey_data['Natural_Ingredients_Preference'].sum() / len(survey_data)) * 100
print(f"Percentage of respondents preferring natural ingredients: {natural_ingredients_preference:.2f}%")

# Calculate willingness to pay for personalized solutions
willingness_to_pay = (survey_data['Willingness_To_Pay'].sum() / len(survey_data)) * 100
print(f"Percentage of respondents willing to pay for personalized solutions: {willingness_to_pay:.2f}%")
