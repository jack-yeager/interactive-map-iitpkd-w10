import folium
from folium import IFrame
import base64

map= folium.Map(location=[10.803489489100986, 76.81870306540125],zoom_start=15)#opens the map need

html= '<img src= "data:image/png;base64,{}">'.format
picture_aeh= base64.b64encode(open(,'rb').read()).decode()
iframe_aeh= IFrame(html(picture_aeh),width=327+20,height=225+20)
popup_aeh= folium.Popup(iframe_aeh,max_width=640)
ricon_aeh= folium.features.CustomIcon('hosp.png',icon_size=(40,40))
folium.Marker(location=[10.794002645395077, 76.82705190698024],tooltip="<strong>Ahalia Eye Hospital</strong>",popup=popup_aeh,icon=ricon_aeh).add_to(map) 

map.save("adh.html")
