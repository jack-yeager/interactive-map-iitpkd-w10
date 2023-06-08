import folium
from folium import IFrame
import base64

map = folium.Map(location=[10.796019890314097,
                 76.82275843702458], zoom_start=16)

html = '<img src= "data:image/png;base64,{}">'.format

picture_vb = base64.b64encode(open('volleyball.jpg', 'rb').read()).decode()
iframe_vb = IFrame(html(picture_vb), width=327+20, height=245+20)
popup_vb = folium.Popup(iframe_vb, max_width=640)
ricon_vb = folium.features.CustomIcon('vb.png', icon_size=(40, 38))
folium.Marker(location=[10.799264150220212, 76.82192429390716],
              tooltip="<strong>Ahalia Volleyball Ground</strong>", popup=popup_vb, icon=ricon_vb).add_to(map)

map.save("volleyball.html")
