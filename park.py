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

picture_l = base64.b64encode(open("./lake.jpg", 'rb').read()).decode()
iframe_l = IFrame(html(picture_l), width=327+20, height=273+20)
popup_l = folium.Popup(iframe_l, max_width=650)
ricon_l = folium.features.CustomIcon('la.png', icon_size=(60, 60))
folium.Marker(location=[10.794969103780806, 76.82528481763399],
              tooltip="<strong>Lake park</strong>", popup=popup_l, icon=ricon_l).add_to(map)

picture3 = base64.b64encode(open("./sculp.jpg", 'rb').read()).decode()
iframe3 = IFrame(html(picture3), width=327+20, height=372+20)
popup3 = folium.Popup(iframe3, max_width=650)
ricon3 = folium.features.CustomIcon('stone.png', icon_size=(40, 40))
folium.Marker(location=[10.795959805319832, 76.82282023370011],
              tooltip="<strong>Ahalia Sculpture Park</strong>", popup=popup3, icon=ricon3).add_to(map)

map.save("park.html")
