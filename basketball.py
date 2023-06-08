import folium
from folium import IFrame
import base64

map = folium.Map(location=[10.796019890314097,
                 76.82275843702458], zoom_start=16)

html = '<img src= "data:image/png;base64,{}">'.format

picture_bk = base64.b64encode(open('basketball.jpg', 'rb').read()).decode()
iframe_bk = IFrame(html(picture_bk), width=327+20, height=245+20)
popup_bk = folium.Popup(iframe_bk, max_width=640)
ricon_bk = folium.features.CustomIcon('bb.png', icon_size=(40, 40))
folium.Marker(location=[10.802793275868506, 76.81854055985796],
              tooltip="<strong>Basketball Court</strong>", popup=popup_bk, icon=ricon_bk).add_to(map)

map.save("bb.html")
