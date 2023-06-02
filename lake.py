import folium
from folium import IFrame
import base64

map= folium.Map(location=[10.803489489100986, 76.81870306540125],zoom_start=15)#opens the map

html= '<img src= "data:image/png;base64,{}">'.format#formating all image files to be added for html

#for location 1: Taste of malabar
picture_l= base64.b64encode(open("./tom.jpg",'rb').read()).decode()#encoding and decoding the image filr
iframe_l= IFrame(html(picture_l),width=327+20,height=160+20)#IFrame used to add picture in popup
popup_l= folium.Popup(iframe_l,max_width=650)
ricon_l= folium.features.CustomIcon('img.png',icon_size=(40,40))#customized food icon
folium.Marker(location=[10.794969103780806, 76.82528481763399],tooltip="<strong>Lake park</strong>",popup=popup_l,icon=ricon_l).add_to(map)#for displaying everything in the given icon
map.save("lake.html")
