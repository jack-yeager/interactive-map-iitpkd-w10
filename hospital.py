import folium
from folium import IFrame
import base64

map = folium.Map(location=[10.796019890314097,
                 76.82275843702458], zoom_start=16)

html = '<img src= "data:image/png;base64,{}">'.format

picture7 = base64.b64encode(open("./adh.jpg", 'rb').read()).decode()
iframe7 = IFrame(html(picture7), width=327+20, height=225+20)
popup7 = folium.Popup(iframe7, max_width=640)
ricon7 = folium.features.CustomIcon('hosp.png', icon_size=(40, 40))
folium.Marker(location=[10.792077430340598, 76.82749318189833],
              tooltip="<strong>Ahalia Diabetic Hospital</strong>", popup=popup7, icon=ricon7).add_to(map)

picture8 = base64.b64encode(open("./ayur.jpg", 'rb').read()).decode()
iframe8 = IFrame(html(picture8), width=327+20, height=170+20)
popup8 = folium.Popup(iframe8, max_width=640)
ricon8 = folium.features.CustomIcon('hosp.png', icon_size=(40, 40))
folium.Marker(location=[10.791929710674356, 76.82899214327897],
              tooltip="<strong>Ahalia Ayurveda Hospital</strong>", popup=popup8, icon=ricon8).add_to(map)

picture_aeh = base64.b64encode(open('aeh.jpg', 'rb').read()).decode()
iframe_aeh = IFrame(html(picture_aeh), width=327+20, height=208+20)
popup_aeh = folium.Popup(iframe_aeh, max_width=640)
ricon_aeh = folium.features.CustomIcon('hosp.png', icon_size=(40, 40))
folium.Marker(location=[10.794002645395077, 76.82705190698024],
              tooltip="<strong>Ahalia Eye Hospital</strong>", popup=popup_aeh, icon=ricon_aeh).add_to(map)

map.save("hopital.html")
