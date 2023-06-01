import folium
from folium import IFrame
import base64

map= folium.Map(location=[10.803489489100986, 76.81870306540125],zoom_start=15)#opens the map

html= '<img src= "data:image/png;base64,{}">'.format#formating all image files to be added for html

#for location 1: Taste of malabar
picture_man= base64.b64encode(open(,'rb').read()).decode()#encoding and decoding the image filr
iframe_man= IFrame(html(picture_man),width=327+20,height=160+20)#IFrame used to add picture in popup
popup_man= folium.Popup(iframe_man,max_width=650)
ricon_man= folium.features.CustomIcon('img.png',icon_size=(40,40))#customized food icon
folium.Marker(location=[10.80179085287843, 76.81853945877002],tooltip="<strong>MANJU CANTEEN</strong>",popup=popup_man,icon=ricon_man).add_to(map)#for displaying everything in the given icon
map.save("manju.html")
