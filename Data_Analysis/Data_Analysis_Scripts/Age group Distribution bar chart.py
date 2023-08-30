import matplotlib.pyplot as plt

# Sample data: Age group distribution of survey respondents
age_groups = ['18-25', '26-35', '36-45', '46-55', '56+']
respondents_count = [120, 180, 90, 60, 40]

# Create a bar chart
plt.bar(age_groups, respondents_count, color='blue')

# Add labels and title
plt.xlabel('Age Group')
plt.ylabel('Number of Respondents')
plt.title('Distribution of Survey Respondents by Age Group')

# Show the chart
plt.show()
