import folium
from folium import IFrame
import base64

map= folium.Map(location=[10.803489489100986, 76.81870306540125],zoom_start=15)

html= '<img src= "data:image/png;base64,{}">'.format

picture_tom= base64.b64encode(open("./tom.jpg",'rb').read()).decode()
iframe_tom= IFrame(html(picture1),width=327+20,height=160+20)
popup_tom= folium.Popup(iframe1,max_width=650)
ricon_tom= folium.features.CustomIcon('img.png',icon_size=(40,40))
folium.Marker(location=[10.799134430915721, 76.81813182028293],tooltip="<strong>Taste of Malabar</strong>",popup=popup_tom,icon=ricon_tom).add_to(map)

map.save("tom.html")
