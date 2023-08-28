import pandas as pd
import matplotlib.pyplot as plt


# Load survey data from CSV file
survey_data = pd.read_csv('C:/Users/Rosha/OneDrive/Documents/Market research on new market entry/data_analysis/survey_data.csv - Sheet1.csv')


# Descriptive statistics
descriptive_stats = survey_data.describe()


# Data visualization: Histogram of Age
plt.figure(figsize=(10, 6))
plt.hist(survey_data['Age'], bins=10, color='blue', alpha=0.7)
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Distribution of Participant Ages')
plt.savefig('C:/Users/Rosha/OneDrive/Documents/Market research on new market entry/data_analysis/visualizations/histogram_age.png')  # Save the visualization
plt.close()


# Calculate preferences for natural ingredients
natural_ingredients_preference = (survey_data['Natural_Ingredients_Preference'].sum() / len(survey_data)) * 100


# Calculate willingness to pay for personalized solutions
willingness_to_pay = (survey_data['Willingness_To_Pay'].sum() / len(survey_data)) * 100


# Save analysis results to a text file
with open('C:/Users/Rosha/OneDrive/Documents/Market research on new market entry/data_analysis/data_analysis_results.txt', 'w') as f:
    f.write("Descriptive Statistics:\n")
    f.write(descriptive_stats.to_string())
    f.write("\n")
    f.write(f"Percentage of respondents preferring natural ingredients: {natural_ingredients_preference:.2f}%\n")
    f.write(f"Percentage of respondents willing to pay for personalized solutions: {willingness_to_pay:.2f}%\n")


print("Analysis completed and results saved.")