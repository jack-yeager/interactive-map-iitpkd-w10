import folium
from folium import IFrame
import base64

map = folium.Map(location=[10.796019890314097,
                 76.82275843702458], zoom_start=16)

html = '<img src= "data:image/png;base64,{}">'.format

picture6 = base64.b64encode(open("./hc.jpg", 'rb').read()).decode()
iframe6 = IFrame(html(picture6), width=327+20, height=187+20)
popup6 = folium.Popup(iframe6, max_width=640)
ricon6 = folium.features.CustomIcon('shop.png', icon_size=(60, 60))
folium.Marker(location=[10.792340364052299, 76.82816306640642],
              tooltip="<strong>Ahalia Home Centre</strong>", popup=popup6, icon=ricon6).add_to(map)

picture_man = base64.b64encode(open('manju.jpg', 'rb').read()).decode()
iframe_man = IFrame(html(picture_man), width=327+20, height=245+20)
popup_man = folium.Popup(iframe_man, max_width=650)
ricon_man = folium.features.CustomIcon('shop.png', icon_size=(60, 60))
folium.Marker(location=[10.801940636611368, 76.81835829549671],
              tooltip="<strong>Manju's Canteen</strong>", popup=popup_man, icon=ricon_man).add_to(map)

map.save("grocery.html")
