import folium
from folium import IFrame
import base64

map= folium.Map(location=[10.803489489100986, 76.81870306540125],zoom_start=15)#opens the map need

html= '<img src= "data:image/png;base64,{}">'.format
picture_ac= base64.b64encode(open(,'rb').read()).decode()
iframe_ac= IFrame(html(picture_ac),width=327+20,height=225+20)
popup_ac= folium.Popup(iframe_ac,max_width=640)
ricon_ac= folium.features.CustomIcon('hosp.png',icon_size=(40,40))
folium.Marker(location=[10.804495144165514, 76.81946710215931],tooltip="<strong>Canara Bank ATM</strong>",popup=popup_ac,icon=ricon_ac).add_to(map) 
map.save("ac.html")
