import folium
from folium import IFrame
import base64

map= folium.Map(location=[10.803489489100986, 76.81870306540125],zoom_start=15)

html= '<img src= "data:image/png;base64,{}">'.format
picture6= base64.b64encode(open("./hc.jpg",'rb').read()).decode()
iframe6= IFrame(html(picture6),width=327+20,height=187+20)
popup6= folium.Popup(iframe6,max_width=640)
ricon6= folium.features.CustomIcon('shop.png',icon_size=(70,70))
folium.Marker(location=[10.792340364052299, 76.82816306640642],tooltip="<strong>Ahalia Home Centre</strong>",popup=popup6,icon=ricon6).add_to(map)

map.save("ahc.html")
