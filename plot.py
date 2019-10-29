import folium
import os
import webbrowser

cur_path = os.getcwd()
file_path = os.path.join(cur_path, "index.html")

m = folium.Map(location=[69.680, 18.95])

data_points = {}

with open("studentdata.csv") as f:
    f.readline()
    for line in f:
        elements = line.split(",")
        data_points[elements[0]] = {'pos': (elements[1], elements[2]), 'pm25': float(elements[4])}

for d in data_points.values():
    pos = d['pos']
    intensity = d['pm25'] / 15
    rgb_intensity = int(intensity * 255)
    rgb_intensiry = min(255, rgb_intensity)
    red_color = hex(rgb_intensity)[2:]
    green_color = hex(255-rgb_intensity)[2:]
    folium.CircleMarker(
            location = [float(pos[0]), float(pos[1])],
            radius = 10,
            color = "#" +red_color + green_color + "00",
            fill = True,
            fill_color = "#" +red_color + green_color + "00"
    ).add_to(m)

m.save(file_path)

webbrowser.open("file://" + file_path)

