import folium
from folium import IFrame
import base64

map = folium.Map(location=[10.796019890314097,
                 76.82275843702458], zoom_start=16)

html = '<img src= "data:image/png;base64,{}">'.format

picture_h3 = base64.b64encode(open("./h3.jpg", 'rb').read()).decode()
iframe_h3 = IFrame(html(picture_h3), width=327+20, height=245+20)
popup_h3 = folium.Popup(iframe_h3, max_width=650)
ricon = folium.features.CustomIcon('home.png', icon_size=(60, 60))
folium.Marker(location=[10.797984370712905, 76.81832584827522],
              tooltip="<strong>Hostel 3</strong>", popup=popup_h3, icon=ricon).add_to(map)

map.save("h3.html")
