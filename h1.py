import folium
from folium import IFrame
import base64

map = folium.Map(location=[10.796019890314097,
                 76.82275843702458], zoom_start=16)

html = '<img src= "data:image/png;base64,{}">'.format

picture_h1 = base64.b64encode(open("./h1.jpg", 'rb').read()).decode()
iframe_h1 = IFrame(html(picture_h1), width=327+20, height=245+20)
popup_h1 = folium.Popup(iframe_h1, max_width=650)
ricon_h1 = folium.features.CustomIcon('home.png', icon_size=(60, 60))
folium.Marker(location=[10.799205621030923, 76.82223021773736],
              tooltip="<strong>Hostel 1</strong>", popup=popup_h1, icon=ricon_h1).add_to(map)

map.save("h1.html")
