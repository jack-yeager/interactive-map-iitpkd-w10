import folium
from folium import IFrame
import base64

# opens the map need
map = folium.Map(location=[10.803489489100986,
                 76.81870306540125], zoom_start=15)

html = '<img src= "data:image/png;base64,{}">'.format

# encoding and decoding the image file
picture1 = base64.b64encode(open("./tom.jpg", 'rb').read()).decode()
iframe1 = IFrame(html(picture1), width=327+20, height=160 +
                 20)  # IFrame used to add picture in popup
popup1 = folium.Popup(iframe1, max_width=650)
ricon = folium.features.CustomIcon(
    'img.png', icon_size=(40, 40))  # customized food icon
folium.Marker(location=[10.799134430915721, 76.81813182028293],
              tooltip="<strong>Taste of Malabar</strong>", popup=popup1, icon=ricon).add_to(map)

picture4 = base64.b64encode(open("./download.jpeg", 'rb').read()).decode()
iframe4 = IFrame(html(picture4), width=259+20, height=194+20)
popup4 = folium.Popup(iframe4, max_width=650)
ricon4 = folium.features.CustomIcon('img.png', icon_size=(40, 40))
folium.Marker(location=[10.800102523261407, 76.81888433684003],
              tooltip="<strong>Cafe Coffee Day</strong>", popup=popup4, icon=ricon4).add_to(map)

picture5 = base64.b64encode(open("./afp1.jpg", 'rb').read()).decode()
iframe5 = IFrame(html(picture5), width=327+20, height=242+20)
popup5 = folium.Popup(iframe5, max_width=640)
ricon5 = folium.features.CustomIcon('img.png', icon_size=(40, 40))
folium.Marker(location=[10.792262269988168, 76.82803937041948],
              tooltip="<strong>Ahalia Food Point</strong>", popup=popup5, icon=ricon5).add_to(map)

picture_mess = base64.b64encode(open('./mess.jpg', 'rb').read()).decode()
iframe_mess = IFrame(html(picture_mess), width=327+20, height=245+20)
popup_mess = folium.Popup(iframe_mess, max_width=650)
ricon_mess = folium.features.CustomIcon('img.png', icon_size=(40, 40))
folium.Marker(location=[10.799290457287118, 76.82241465360843],
              tooltip="<strong>Mess</strong>", popup=popup_mess, icon=ricon_mess).add_to(map)

map.save("food places.html")
