import folium
from folium import IFrame
import base64

map = folium.Map(location=[10.796019890314097,
                 76.82275843702458], zoom_start=16)

html = '<img src= "data:image/png;base64,{}">'.format


picture_vb = base64.b64encode(open('volleyball.jpg', 'rb').read()).decode()
iframe_vb = IFrame(html(picture_vb), width=327+20, height=245+20)
popup_vb = folium.Popup(iframe_vb, max_width=640)
ricon_vb = folium.features.CustomIcon('vb.png', icon_size=(40, 38))
folium.Marker(location=[10.799264150220212, 76.82192429390716],
              tooltip="<strong>Ahalia Volleyball Ground</strong>", popup=popup_vb, icon=ricon_vb).add_to(map)

picture2 = base64.b64encode(open("./ahaliafb.jpg", 'rb').read()).decode()
iframe2 = IFrame(html(picture2), width=327+20, height=218+20)
popup2 = folium.Popup(iframe2, max_width=640)
ricon2 = folium.features.CustomIcon('football.png', icon_size=(40, 40))
folium.Marker(location=[10.802291523435375, 76.81926446770233],
              tooltip="<strong>Ahalia Football Ground</strong>", popup=popup2, icon=ricon2).add_to(map)

picture_bk = base64.b64encode(open('basketball.jpg', 'rb').read()).decode()
iframe_bk = IFrame(html(picture_bk), width=327+20, height=245+20)
popup_bk = folium.Popup(iframe_bk, max_width=640)
ricon_bk = folium.features.CustomIcon('bb.png', icon_size=(40, 40))
folium.Marker(location=[10.802793275868506, 76.81854055985796],
              tooltip="<strong>Basketball Court</strong>", popup=popup_bk, icon=ricon_bk).add_to(map)

map.save("sport.html")
