import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Sample text data
text_data = """
Health and wellness products are in demand.
Consumers prefer natural ingredients in their supplements.
Vitamins, herbs, and protein supplements are popular choices.
Market entry strategies should focus on consumer preferences.
Wellness trends include personalized solutions and holistic approaches.
"""

# Generate a word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text_data)

# Display the word cloud using matplotlib
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
