import folium
from folium import IFrame
import base64

map= folium.Map(location=[10.803489489100986, 76.81870306540125],zoom_start=15)#opens the map

html= '<img src= "data:image/png;base64,{}">'.format#formating all image files to be added for html

#for location 1: Taste of malabar
picture_cdc= base64.b64encode(open(,'rb').read()).decode()#encoding and decoding the image filr
iframe_cdc= IFrame(html(picture_cdc),width=327+20,height=160+20)#IFrame used to add picture in popup
popup_cdc= folium.Popup(iframe_cdc,max_width=650)
ricon_cdc= folium.features.CustomIcon('img.png',icon_size=(40,40))#customized food icon
folium.Marker(location=[10.80002997087941, 76.81874784806095],tooltip="<strong>Taste of Malabar</strong>",popup=popup_cdc,icon=ricon_cdc).add_to(map)#for displaying everything in the given icon
map.save("cdc.html")
