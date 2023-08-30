import matplotlib.pyplot as plt

# Sample data: Wellness product preferences
products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
preferences_percentage = [25, 20, 15, 25, 15]

# Create a pie chart
plt.pie(preferences_percentage, labels=products, autopct='%1.1f%%', startangle=140)

# Equal aspect ratio ensures that pie is drawn as a circle.
plt.axis('equal')

# Add title
plt.title('Percentage Distribution of Preferences for Wellness Products')

# Show the chart
plt.show()
