import folium
from folium import IFrame
import base64

map = folium.Map(location=[10.796019890314097,
                 76.82275843702458], zoom_start=16)

html = '<img src= "data:image/png;base64,{}">'.format

picture_mess = base64.b64encode(open('./mess.jpg', 'rb').read()).decode()
iframe_mess = IFrame(html(picture_mess), width=327+20, height=245+20)
popup_mess = folium.Popup(iframe_mess, max_width=650)
ricon_mess = folium.features.CustomIcon('img.png', icon_size=(40, 40))
folium.Marker(location=[10.799290457287118, 76.82241465360843],
              tooltip="<strong>Mess</strong>", popup=popup_mess, icon=ricon_mess).add_to(map)

map.save("mess.html")
