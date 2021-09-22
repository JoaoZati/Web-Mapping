import folium

map = folium.Map(location=[38.58, -99.09], zoom_start=6)

fg = folium.FeatureGroup(name="Map")

coordinates = [[38.58, -99.09], [39.58, -97.09], [40, -100]]
for coordinate in coordinates:
    fg.add_child(folium.Marker(location=coordinate, popup="Marker", icon=folium.Icon('green')))

map.add_child(fg)

map.save("index.html")
