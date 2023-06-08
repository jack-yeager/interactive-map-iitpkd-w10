import folium
from folium import IFrame
import base64

map = folium.Map(location=[10.796019890314097,
                 76.82275843702458], zoom_start=16)

html = '<img src= "data:image/png;base64,{}">'.format

# Hostel 1
picture_h1 = base64.b64encode(open("./h1.jpg", 'rb').read()).decode()
iframe_h1 = IFrame(html(picture_h1), width=327+20, height=245+20)
popup_h1 = folium.Popup(iframe_h1, max_width=650)
ricon_h1 = folium.features.CustomIcon('home.png', icon_size=(60, 60))
folium.Marker(location=[10.799205621030923, 76.82223021773736],
              tooltip="<strong>Hostel 1</strong>", popup=popup_h1, icon=ricon_h1).add_to(map)

# Hostel 2
picture_h2 = base64.b64encode(open('./h2.jpg', 'rb').read()).decode()
iframe_h2 = IFrame(html(picture_h2), width=327+20, height=245+20)
popup_h2 = folium.Popup(iframe_h2, max_width=650)
ricon_h2 = folium.features.CustomIcon('home.png', icon_size=(60, 60))
folium.Marker(location=[10.799550455187008, 76.8222669062808],
              tooltip="<strong>Hostel 2</strong>", popup=popup_h2, icon=ricon_h2).add_to(map)

# Hostel 3
picture_h3 = base64.b64encode(open("./h3.jpg", 'rb').read()).decode()
iframe_h3 = IFrame(html(picture_h3), width=327+20, height=245+20)
popup_h3 = folium.Popup(iframe_h3, max_width=650)
ricon = folium.features.CustomIcon('home.png', icon_size=(60, 60))
folium.Marker(location=[10.797984370712905, 76.81832584827522],
              tooltip="<strong>Hostel 3</strong>", popup=popup_h3, icon=ricon).add_to(map)


map.save("hostel.html")
