import folium
from folium import IFrame
import base64

# opens the map need
map = folium.Map(location=[10.803489489100986,
                 76.81870306540125], zoom_start=15)

html = '<img src= "data:image/png;base64,{}">'.format
picture7 = base64.b64encode(open("./adh.jpg", 'rb').read()).decode()
iframe7 = IFrame(html(picture7), width=327+20, height=225+20)
popup7 = folium.Popup(iframe7, max_width=640)
ricon7 = folium.features.CustomIcon('hosp.png', icon_size=(40, 40))
folium.Marker(location=[10.792077430340598, 76.82749318189833],
              tooltip="<strong>Ahalia Diabetic Hospital</strong>", popup=popup7, icon=ricon7).add_to(map)

map.save("adh.html")
