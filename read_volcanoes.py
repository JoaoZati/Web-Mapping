import folium

list_vulcao = []
with open('Volcanoes.txt', 'r') as file:
    for line in file.readlines():
        line = line.strip()
        list_vulcao.append(line.split(','))

lat_long = [i[-2:] for i in list_vulcao]
lat_long = lat_long[1:]
for i, valuei in enumerate(lat_long):
    for j, valuej in enumerate(valuei):
        lat_long[i][j] = float(valuej)

map = folium.Map()
fg = folium.FeatureGroup(name="My map")

coordinates = lat_long
for coordinate in coordinates:
    fg.add_child(folium.Marker(location=coordinate, popup="Marker", icon=folium.Icon('green')))

map.add_child(fg)

map.save("Map_vulcao.html")
