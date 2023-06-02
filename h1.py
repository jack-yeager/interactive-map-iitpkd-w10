import folium
from folium import IFrame
import base64

map= folium.Map(location=[10.803489489100986, 76.81870306540125],zoom_start=15)#opens the map

html= '<img src= "data:image/png;base64,{}">'.format#formating all image files to be added for html

#for location 1: Taste of malabar
picture_h1= base64.b64encode(open("./tom.jpg",'rb').read()).decode()#encoding and decoding the image filr
iframe_h1= IFrame(html(picture_h1),width=327+20,height=160+20)#IFrame used to add picture in popup
popup_h1= folium.Popup(iframe_h1,max_width=650)
ricon_h1= folium.features.CustomIcon('img.png',icon_size=(40,40))#customized food icon
folium.Marker(location=[10.799205621030923, 76.82223021773736],tooltip="<strong>Hostel 1</strong>",popup=popup_h1,icon=ricon_h1).add_to(map)#for displaying everything in the given icon
map.save("h1.html")
