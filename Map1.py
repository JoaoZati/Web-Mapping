import folium

map = folium.Map(location=[38.58, -99.09], zoom_start=6)

fg = folium.FeatureGroup(name="My map")
fg.add_child(folium.Marker(location=[38.58, -99.09], popup="Marker", icon=folium.Icon('green')))
map.add_child(fg)

map.save("Map1.html")
