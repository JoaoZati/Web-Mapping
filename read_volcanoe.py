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

data = open('world.json', 'r', encoding='utf-8-sig').read()
fg.add_child(folium.GeoJson(data=data, style_function=lambda x: {'fillColor':
                                                                 'green' if x['properties']['POP2005'] < 10_000_000
                                                                 else 'orange' if 10_000_000 <= x['properties']['POP2005'] <= 20_000_000
                                                                 else 'red'}))

map.add_child(fg)
map.save("Map_vulcao.html")
