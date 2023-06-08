import folium
from folium import IFrame
import base64

map = folium.Map(location=[10.796019890314097,
                 76.82275843702458], zoom_start=16)

html = '<img src= "data:image/png;base64,{}">'.format

picture_mba = base64.b64encode(open('mba.jpg', 'rb').read()).decode()
iframe_mba = IFrame(html(picture_mba), width=327+20, height=245+20)
popup_mba = folium.Popup(iframe_mba, max_width=650)
ricon_mba = folium.features.CustomIcon('lib.png', icon_size=(40, 60))
folium.Marker(location=[10.799334989848212, 76.82103835492995],
              tooltip="<strong>MBA Block</strong>", popup=popup_mba, icon=ricon_mba).add_to(map)

map.save("mba.html")
