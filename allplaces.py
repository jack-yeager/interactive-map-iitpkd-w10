import folium
from folium import IFrame
import base64

map= folium.Map(location=[10.803489489100986, 76.81870306540125],zoom_start=15)#opens the map

html= '<img src= "data:image/png;base64,{}">'.format#formating all image files to be added for html

#for location 1: Taste of malabar
picture1= base64.b64encode(open("./tom.jpg",'rb').read()).decode()#encoding and decoding the image filr
iframe1= IFrame(html(picture1),width=327+20,height=160+20)#IFrame used to add picture in popup
popup1= folium.Popup(iframe1,max_width=650)
ricon= folium.features.CustomIcon('img.png',icon_size=(40,40))#customized food icon
folium.Marker(location=[10.799134430915721, 76.81813182028293],tooltip="<strong>Taste of Malabar</strong>",popup=popup1,icon=ricon).add_to(map)#for displaying everything in the given icon


#for location 2: Ahalia foodball ground
picture2= base64.b64encode(open("./ahaliafb.jpg",'rb').read()).decode()
iframe2= IFrame(html(picture2),width=640+20,height=427+20)
popup2= folium.Popup(iframe2,max_width=650)
ricon2= folium.features.CustomIcon('football.png',icon_size=(40,40))
folium.Marker(location=[10.802291523435375, 76.81926446770233],tooltip="<strong>Ahalia Football Ground</strong>",popup=popup2,icon=ricon2).add_to(map)


#for location 3: Ahalia Rock Garden
picture3= base64.b64encode(open("./sculp.jpg",'rb').read()).decode()
iframe3= IFrame(html(picture3),width=327+20,height=284+20)
popup3= folium.Popup(iframe3,max_width=650)
ricon3= folium.features.CustomIcon('stone.png',icon_size=(40,40))
folium.Marker(location=[10.797272401469742, 76.82453931753778],tooltip="<strong>Ahalia Rock Garden</strong>",popup=popup3,icon=ricon3).add_to(map)

#for location 4: Cafe Coffee Day Bevarages
picture4= base64.b64encode(open("./download.jpeg",'rb').read()).decode()
iframe4= IFrame(html(picture1),width=327+20,height=160+20)
popup4= folium.Popup(iframe1,max_width=650)
ricon4= folium.features.CustomIcon('img.png',icon_size=(40,40))
folium.Marker(location=[10.800102523261407, 76.81888433684003],tooltip="<strong>Cafe Coffee Day</strong>",popup=popup4,icon=ricon4).add_to(map)

#for location 5: 

map.save("all_places.html")
