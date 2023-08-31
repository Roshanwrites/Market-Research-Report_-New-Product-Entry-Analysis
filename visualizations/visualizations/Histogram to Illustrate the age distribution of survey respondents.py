import matplotlib.pyplot as plt

# Sample data: Ages of survey respondents
ages = [25, 28, 30, 35, 40, 42, 45, 50, 55, 60, 65, 70, 75, 80, 85]

# Create a histogram
plt.hist(ages, bins=10, edgecolor='black')

# Add title and labels
plt.title('Age Distribution of Survey Respondents')
plt.xlabel('Age')
plt.ylabel('Frequency')

# Show the histogram
plt.grid(True)
plt.show()
