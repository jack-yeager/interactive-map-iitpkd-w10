import folium
from folium import IFrame
import base64

map = folium.Map(location=[10.796019890314097,
                 76.82275843702458], zoom_start=16)

html = '<img src= "data:image/png;base64,{}">'.format

picture_ph = base64.b64encode(open('pharm.jpg', 'rb').read()).decode()
iframe_ph = IFrame(html(picture_ph), width=325+20, height=277+20)
popup_ph = folium.Popup(iframe_ph, max_width=650)
ricon_ph = folium.features.CustomIcon('lib.png', icon_size=(40, 60))
folium.Marker(location=[10.800699183782722, 76.81830260137629],
              tooltip="<strong>Pharmacy Block</strong>", popup=popup_ph, icon=ricon_ph).add_to(map)

map.save("pharm.html")
