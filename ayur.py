import folium
from folium import IFrame
import base64

map= folium.Map(location=[10.803489489100986, 76.81870306540125],zoom_start=15)#opens the map need

html= '<img src= "data:image/png;base64,{}">'.format
picture8= base64.b64encode(open("./ayur.jpg",'rb').read()).decode()
iframe8= IFrame(html(picture8),width=327+20,height=225+20)
popup8= folium.Popup(iframe8,max_width=640)
ricon8= folium.features.CustomIcon('hosp.png',icon_size=(40,40))
folium.Marker(location=[10.792077430340598, 76.82749318189833],tooltip="<strong>Ahalia Ayurveda Hospital</strong>",popup=popup8,icon=ricon8).add_to(map) 
map.save("ayur.html")
