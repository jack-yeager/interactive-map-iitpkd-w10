import folium
from folium import IFrame
import base64

map = folium.Map(location=[10.796019890314097,
                 76.82275843702458], zoom_start=16)

html = '<img src= "data:image/png;base64,{}">'.format

picture_man = base64.b64encode(open('manju.jpg', 'rb').read()).decode()
iframe_man = IFrame(html(picture_man), width=327+20, height=245+20)
popup_man = folium.Popup(iframe_man, max_width=650)
ricon_man = folium.features.CustomIcon('shop.png', icon_size=(60, 60))
folium.Marker(location=[10.801940636611368, 76.81835829549671],
              tooltip="<strong>Manju's Canteen</strong>", popup=popup_man, icon=ricon_man).add_to(map)

map.save("manju.html")
