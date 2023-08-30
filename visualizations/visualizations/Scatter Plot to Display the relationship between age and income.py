import matplotlib.pyplot as plt

# Sample data: Age and corresponding income of survey respondents
ages = [25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
income = [50000, 60000, 75000, 80000, 90000, 95000, 100000, 105000, 110000, 120000]

# Create a scatter plot
plt.scatter(ages, income, color='blue', marker='o', label='Survey Data')

# Add title and labels
plt.title('Relationship between Age and Income')
plt.xlabel('Age')
plt.ylabel('Income')

# Add legend
plt.legend()

# Show the scatter plot
plt.grid(True)
plt.show()
