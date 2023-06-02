import folium
from folium import IFrame
import base64

map= folium.Map(location=[10.803489489100986, 76.81870306540125],zoom_start=15)#opens the map need

html= '<img src= "data:image/png;base64,{}">'.format
picture_bk= base64.b64encode(open(,'rb').read()).decode()
iframe_bk= IFrame(html(picture_bk),width=327+20,height=225+20)
popup_bk= folium.Popup(iframe_bk,max_width=640)
ricon_bk= folium.features.CustomIcon('hosp.png',icon_size=(40,40))
folium.Marker(location=[10.802793275868506, 76.81854055985796],tooltip="<strong>Basketball Court</strong>",popup=popup_bk,icon=ricon_bk).add_to(map) 
map.save("bk.html")
