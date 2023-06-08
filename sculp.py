import folium
from folium import IFrame
import base64

map = folium.Map(location=[10.803489489100986,
                 76.81870306540125], zoom_start=15)

html = '<img src= "data:image/png;base64,{}">'.format

picture3 = base64.b64encode(open("./sculp.jpg", 'rb').read()).decode()
iframe3 = IFrame(html(picture3), width=327+20, height=372+20)
popup3 = folium.Popup(iframe3, max_width=650)
ricon3 = folium.features.CustomIcon('stone.png', icon_size=(40, 40))
folium.Marker(location=[10.795959805319832, 76.82282023370011],
              tooltip="<strong>Ahalia Sculpture Park</strong>", popup=popup3, icon=ricon3).add_to(map)

map.save("sculp.html")
