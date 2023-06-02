import folium
from folium import IFrame
import base64

map= folium.Map(location=[10.803489489100986, 76.81870306540125],zoom_start=15)#opens the map need

html= '<img src= "data:image/png;base64,{}">'.format
picture_ayur= base64.b64encode(open(,'rb').read()).decode()
iframe_ayur= IFrame(html(picture_ayur),width=327+20,height=225+20)
popup_ayur= folium.Popup(iframe_ayur,max_width=640)
ricon_ayur= folium.features.CustomIcon('hosp.png',icon_size=(40,40))
folium.Marker(location=[10.7918780238658, 76.8297160664962],tooltip="<strong>Ahalia Ayurveda Hospital</strong>",popup=popup_adh,icon=ricon_adh).add_to(map) 
map.save("ayur.html")
