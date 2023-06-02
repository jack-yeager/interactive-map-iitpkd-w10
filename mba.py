import folium
from folium import IFrame
import base64

map= folium.Map(location=[10.803489489100986, 76.81870306540125],zoom_start=15)#opens the map

html= '<img src= "data:image/png;base64,{}">'.format#formating all image files to be added for html

#for location 1: Taste of malabar
picture_mba= base64.b64encode(open(,'rb').read()).decode()#encoding and decoding the image filr
iframe_mba= IFrame(html(picture_mba),width=327+20,height=160+20)#IFrame used to add picture in popup
popup_mba= folium.Popup(iframe_mba,max_width=650)
ricon_mba= folium.features.CustomIcon('img.png',icon_size=(40,40))#customized food icon
folium.Marker(location=[10.799290457287118, 76.82241465360843],tooltip="<strong>MBA Block</strong>",popup=popup_mba,icon=ricon_mba).add_to(map)#for displaying everything in the given icon
map.save("mba.html")
