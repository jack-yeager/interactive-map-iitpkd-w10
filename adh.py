import folium
from folium import IFrame
import base64

map= folium.Map(location=[10.803489489100986, 76.81870306540125],zoom_start=15)#opens the map need

html= '<img src= "data:image/png;base64,{}">'.format
picture_adh= base64.b64encode(open(,'rb').read()).decode()
iframe_adh= IFrame(html(picture_adh),width=327+20,height=225+20)
popup_adh= folium.Popup(iframe_adh,max_width=640)
ricon_adh= folium.features.CustomIcon('hosp.png',icon_size=(40,40))
folium.Marker(location=[10.79221717547408, 76.82741136465046],tooltip="<strong>Ahalia Diabetic Hospital</strong>",popup=popup_adh,icon=ricon_adh).add_to(map) 

map.save("adh.html")
