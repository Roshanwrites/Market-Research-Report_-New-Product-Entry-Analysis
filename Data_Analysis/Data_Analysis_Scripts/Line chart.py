import matplotlib.pyplot as plt

# Sample data: Years and consumer interest scores
years = [2018, 2019, 2020, 2021, 2022, 2023]
interest_scores = [50, 55, 60, 65, 70, 75]

# Create a line chart
plt.plot(years, interest_scores, marker='o')

# Add title and labels
plt.title('Trend in Consumer Interest in Health and Wellness Products')
plt.xlabel('Year')
plt.ylabel('Interest Score')

# Show the chart
plt.grid(True)
plt.show()
