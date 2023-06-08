import folium
from folium import IFrame
import base64

map = folium.Map(location=[10.796019890314097,
                 76.82275843702458], zoom_start=16)

html = '<img src= "data:image/png;base64,{}">'.format

picture_l = base64.b64encode(open("./lake.jpg", 'rb').read()).decode()
iframe_l = IFrame(html(picture_l), width=327+20, height=273+20)
popup_l = folium.Popup(iframe_l, max_width=650)
ricon_l = folium.features.CustomIcon('la.png', icon_size=(60, 60))
folium.Marker(location=[10.794969103780806, 76.82528481763399],
              tooltip="<strong>Lake park</strong>", popup=popup_l, icon=ricon_l).add_to(map)

map.save("lake.html")
