import folium
from folium import IFrame
import base64

map= folium.Map(location=[10.803489489100986, 76.81870306540125],zoom_start=15)#opens the map

html= '<img src= "data:image/png;base64,{}">'.format#formating all image files to be added for html

#for location : h3
picture_h3= base64.b64encode(open("./tom.jpg",'rb').read()).decode()#encoding and decoding the image filr
iframe_h3= IFrame(html(picture_h3),width=327+20,height=160+20)#IFrame used to add picture in popup
popup_h3= folium.Popup(iframe_h3,max_width=650)
ricon= folium.features.CustomIcon('img.png',icon_size=(40,40))#customized hostel icon
folium.Marker(location=[10.797984370712905, 76.81832584827522],tooltip="<strong>Hostel 3</strong>",popup=popup_h3,icon=ricon).add_to(map)#for displaying everything in the given icon
map.save("h3.html")
