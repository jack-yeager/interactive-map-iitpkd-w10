import folium
from folium import IFrame
import base64

map = folium.Map(location=[10.796019890314097,
                 76.82275843702458], zoom_start=16)

html = '<img src= "data:image/png;base64,{}">'.format

picture_ac = base64.b64encode(open('canara.jpg', 'rb').read()).decode()
iframe_ac = IFrame(html(picture_ac), width=327+20, height=437+20)
popup_ac = folium.Popup(iframe_ac, max_width=640)
ricon_ac = folium.features.CustomIcon('bank.png', icon_size=(40, 40))
folium.Marker(location=[10.800427387710556, 76.81835704549528],
              tooltip="<strong>Canara Bank ATM</strong>", popup=popup_ac, icon=ricon_ac).add_to(map)

map.save("canara.html")
