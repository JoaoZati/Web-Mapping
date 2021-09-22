import folium
import pandas as pd

data = pd.read_csv("Volcanoes.txt")
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])


def color_producer(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation <= 3000:
        return "orange"
    return "red"


map = folium.Map()
fg = folium.FeatureGroup(name="My map")

for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.Marker(location=[lt, ln], popup=str(el) + ' m', icon=folium.Icon(color_producer(el))))

map.add_child(fg)

map.save("Map_vulcao.html")