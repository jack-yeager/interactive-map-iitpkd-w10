import folium
from folium import IFrame
import base64

map = folium.Map(location=[10.796019890314097,
                 76.82275843702458], zoom_start=16)

html = '<img src= "data:image/png;base64,{}">'.format

picture_stat = base64.b64encode(
    open("statue.jpg", 'rb').read()).decode()  # change
iframe_stat = IFrame(html(picture_stat), width=327+20, height=440+20)
popup_stat = folium.Popup(iframe_stat, max_width=640)
ricon_stat = folium.features.CustomIcon('stone.png', icon_size=(40, 40))
folium.Marker(location=[10.79439732616303, 76.82345431105006],
              tooltip="<strong>Ahalia Statue</strong>", popup=popup_stat, icon=ricon_stat).add_to(map)

map.save("statue.html")
