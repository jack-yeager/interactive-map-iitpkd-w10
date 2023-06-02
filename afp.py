import folium
from folium import IFrame
import base64

map= folium.Map(location=[10.803489489100986, 76.81870306540125],zoom_start=15)#opens the map need

html= '<img src= "data:image/png;base64,{}">'.format
picture_afp= base64.b64encode(open(,'rb').read()).decode()
iframe_afp= IFrame(html(picture_afp),width=327+20,height=225+20)
popup_afp= folium.Popup(iframe_afp,max_width=640)
ricon_afp= folium.features.CustomIcon('hosp.png',icon_size=(40,40))
folium.Marker(location=[10.79225910098684, 76.82801481185315],tooltip="<strong>Ahalia Food point</strong>",popup=popup_afp,icon=ricon_afp).add_to(map) 

map.save("afp.html")
