import numpy as np
import matplotlib.pyplot as plt

# Categories or attributes for the radar chart
categories = ['Product Quality', 'Effectiveness', 'Innovation', 'Affordability', 'Brand Reputation']

# Strengths and weaknesses data (degrees)
strengths = [45, 135, 90, 30, 60]
weaknesses = [120, 60, 75, 105, 135]

# Convert degrees to radians for plotting
strengths = np.radians(strengths)
weaknesses = np.radians(weaknesses)

# Number of categories
num_categories = len(categories)

# Create figure and axes
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw={'projection': 'polar'})

# Plot strengths
ax.plot(strengths, np.ones(num_categories), 'o-', label='Strengths')
ax.fill(strengths, np.ones(num_categories), alpha=0.25)

# Plot weaknesses
ax.plot(weaknesses, np.ones(num_categories), 'o-', label='Weaknesses')
ax.fill(weaknesses, np.ones(num_categories), alpha=0.25)

# Set theta ticks and labels
ax.set_xticks(np.linspace(0, 2*np.pi, num_categories, endpoint=False))
ax.set_xticklabels(categories)

# Set radial gridlines
ax.set_rticks([])  # Hide radial gridlines

# Add a legend
ax.legend()

# Set title
plt.title("Radar Chart: Strengths and Weaknesses")

# Show the plot
plt.show()

