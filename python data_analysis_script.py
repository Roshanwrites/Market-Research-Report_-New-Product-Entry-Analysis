from fpdf import FPDF
import pandas as pd
import matplotlib.pyplot as plt

# Load survey data from CSV file
survey_data = pd.read_csv('survey_data.csv')

# Convert 'Yes' to 1 and 'No' to 0 in 'Natural_Ingredients_Preference' column
survey_data['Natural_Ingredients_Preference'] = survey_data['Natural_Ingredients_Preference'].map({'Yes': 1, 'No': 0})

# Calculate preferences for natural ingredients
natural_ingredients_preference = (survey_data['Natural_Ingredients_Preference'].sum() / len(survey_data)) * 100

# Calculate willingness to pay for personalized solutions
willingness_to_pay = (survey_data['Willingness_To_Pay'].sum() / len(survey_data)) * 100

# Rest of your code...
