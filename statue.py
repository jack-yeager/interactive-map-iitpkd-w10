import folium
from folium import IFrame
import base64

map= folium.Map(location=[10.803489489100986, 76.81870306540125],zoom_start=15)#opens the map need

html= '<img src= "data:image/png;base64,{}">'.format
picture_stat= base64.b64encode(open(,'rb').read()).decode()
iframe_stat= IFrame(html(picture_stat),width=327+20,height=225+20)
popup_stat= folium.Popup(iframe_stat,max_width=640)
ricon_stat= folium.features.CustomIcon('hosp.png',icon_size=(40,40))
folium.Marker(location=[10.794403, 76.823627],tooltip="<strong>Ahalia Statue</strong>",popup=popup_stat,icon=ricon_stat).add_to(map) 
map.save("stat.html")
