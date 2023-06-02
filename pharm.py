import folium
from folium import IFrame
import base64

map= folium.Map(location=[10.803489489100986, 76.81870306540125],zoom_start=15)#opens the map

html= '<img src= "data:image/png;base64,{}">'.format#formating all image files to be added for html

#for location 1: Taste of malabar
picture_ph= base64.b64encode(open(,'rb').read()).decode()#encoding and decoding the image filr
iframe_ph= IFrame(html(picture_ph),width=327+20,height=160+20)#IFrame used to add picture in popup
popup_ph= folium.Popup(iframe_ph,max_width=650)
ricon_ph= folium.features.CustomIcon('img.png',icon_size=(40,40))#customized food icon
folium.Marker(location=[10.800699183782722, 76.81830260137629],tooltip="<strong>Pharmacy Block</strong>",popup=popup_ph,icon=ricon_ph).add_to(map)#for displaying everything in the given icon
map.save("pharm.html")
