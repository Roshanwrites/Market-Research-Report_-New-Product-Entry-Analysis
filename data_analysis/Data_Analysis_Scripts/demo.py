import folium

# Create a base map centered around a specific location
map_center = [20.5937, 78.9629]  # India's approximate coordinates
m = folium.Map(location=map_center, zoom_start=5)

# Placeholder coordinates for store and clinic locations
store_locations = [
    {"name": "Store A", "coordinates": [28.6139, 77.2090]},  # New Delhi
    {"name": "Store B", "coordinates": [19.0760, 72.8777]},  # Mumbai
    {"name": "Store C", "coordinates": [13.0827, 80.2707]},  # Chennai
    {"name": "Store D", "coordinates": [17.3850, 78.4867]},  # Hyderabad
]

clinic_locations = [
    {"name": "Clinic X", "coordinates": [18.5204, 73.8567]},  # Pune
    {"name": "Clinic Y", "coordinates": [12.9716, 77.5946]},  # Bangalore
    {"name": "Clinic Z", "coordinates": [22.5726, 88.3639]},  # Kolkata
]

# Add markers for store locations
for location in store_locations:
    folium.Marker(location["coordinates"], popup=location["name"]).add_to(m)

# Add markers for clinic locations
for location in clinic_locations:
    folium.Marker(location["coordinates"], popup=location["name"]).add_to(m)

# Add heatmap layer for customer density (demo purpose)
heatmap_data = [
    [28.6139, 77.2090, 10],
    [19.0760, 72.8777, 8],
    [18.5204, 73.8567, 6],
    [12.9716, 77.5946, 5],
    [13.0827, 80.2707, 3],
    [17.3850, 78.4867, 4],
    [22.5726, 88.3639, 2],
]
folium.plugins.HeatMap(heatmap_data).add_to(m)

# Add demographic data overlay (demo purpose)
demographic_data = [
    [28.6139, 77.2090, "Age: 25-35, Income: High"],
    [19.0760, 72.8777, "Age: 18-30, Income: Medium"],
    [12.9716, 77.5946, "Age: 25-40, Income: High"],
]
for data in demographic_data:
    folium.Marker(data[:2], popup=data[2], icon=folium.Icon(icon="info-sign")).add_to(m)

# Add competitor locations (demo purpose)
competitor_locations = [
    {"name": "Competitor 1", "coordinates": [28.7041, 77.1025]},  # Delhi
    {"name": "Competitor 2", "coordinates": [18.9750, 72.8258]},  # Mumbai
    {"name": "Competitor 3", "coordinates": [12.9716, 77.5946]},  # Bangalore
]

for location in competitor_locations:
    folium.Marker(location["coordinates"], popup=location["name"], icon=folium.Icon(color="red")).add_to(m)

# Add gyms and wellness centers (demo purpose)
wellness_centers = [
    {"name": "Wellness Center X", "coordinates": [28.7041, 77.1025]},  # Delhi
    {"name": "Wellness Center Y", "coordinates": [18.9750, 72.8258]},  # Mumbai
    {"name": "Wellness Center Z", "coordinates": [17.3850, 78.4867]},  # Hyderabad
]

for location in wellness_centers:
    folium.Marker(location["coordinates"], popup=location["name"], icon=folium.Icon(color="green")).add_to(m)

# Add a layer control to toggle different markers and layers
folium.LayerControl().add_to(m)

# Save the map as an HTML file
m.save('health_wellness_brand_map.html')
