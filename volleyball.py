import folium
from folium import IFrame
import base64

map= folium.Map(location=[10.803489489100986, 76.81870306540125],zoom_start=15)

html= '<img src= "data:image/png;base64,{}">'.format

picture_vb= base64.b64encode(open(,'rb').read()).decode()
iframe_vb= IFrame(html(picture_vb),width=327+20,height=218+20)
popup-vb= folium.Popup(iframe_vb,max_width=640)
ricon_vb= folium.features.CustomIcon('football.png',icon_size=(40,40))
folium.Marker(location=[10.799264150220212, 76.82192429390716],tooltip="<strong>Ahalia Volleyball Ground</strong>",popup=popup_vb,icon=ricon_vb).add_to(map)

map.save("vb.html")

