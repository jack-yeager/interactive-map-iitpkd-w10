import folium
from folium import IFrame
import base64

map= folium.Map(location=[10.803489489100986, 76.81870306540125],zoom_start=15)

html= '<img src= "data:image/png;base64,{}">'.format

picture2= base64.b64encode(open("./ahaliafb.jpg",'rb').read()).decode()
iframe2= IFrame(html(picture2),width=327+20,height=218+20)
popup2= folium.Popup(iframe2,max_width=640)
ricon2= folium.features.CustomIcon('football.png',icon_size=(40,40))
folium.Marker(location=[10.802291523435375, 76.81926446770233],tooltip="<strong>Ahalia Football Ground</strong>",popup=popup2,icon=ricon2).add_to(map)

map.save("afb.html")
