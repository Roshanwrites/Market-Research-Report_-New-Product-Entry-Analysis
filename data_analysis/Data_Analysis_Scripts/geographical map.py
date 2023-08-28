import folium

# Create a map centered at a specific latitude and longitude (India centric)
map_center = [20.5937, 78.9629]  # Coordinates for India
m = folium.Map(location=map_center, zoom_start=5)

# Add markers to the map
folium.Marker([20.5937, 78.9629], popup='India').add_to(m)
folium.Marker([28.6139, 77.2090], popup='New Delhi').add_to(m)
folium.Marker([19.0760, 72.8777], popup='Mumbai').add_to(m)

# Save the map as an HTML file
m.save('geographical_map_india.html')
