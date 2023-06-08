import folium
from folium import IFrame
import base64

map = folium.Map(location=[10.796019890314097,
                 76.82275843702458], zoom_start=16)

html = '<img src= "data:image/png;base64,{}">'.format

picture_ab = base64.b64encode(open('./acad.jpg', 'rb').read()).decode()
iframe_ab = IFrame(html(picture_ab), width=327+20, height=245+20)
popup_ab = folium.Popup(iframe_ab, max_width=650)
ricon_ab = folium.features.CustomIcon('lib.png', icon_size=(40, 60))
folium.Marker(location=[10.8017955754564, 76.81849606364607],
              tooltip="<strong>Academic Block</strong>", popup=popup_ab, icon=ricon_ab).add_to(map)

map.save("acad.html")
