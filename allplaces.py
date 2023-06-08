import folium  # helped to create leaflets map and save them as html file
from folium import IFrame  # helped to add images in popup
import base64  # convert ASCII characters to binary and takes care of encoding and decoding them

# opens the map needed by taking the centre point as the given co-ordinates
map = folium.Map(location=[10.796019890314097,
                 76.82275843702458], zoom_start=16)

# formating all image files to be added for html
html = '<img src= "data:image/png;base64,{}">'.format

# for location 1: Taste of malabar
# encoding and decoding the image file
picture1 = base64.b64encode(open("./tom.jpg", 'rb').read()).decode()
iframe1 = IFrame(html(picture1), width=327+20, height=160 +
                 20)  # IFrame used to add picture in popup
popup1 = folium.Popup(iframe1, max_width=650)
ricon = folium.features.CustomIcon(
    'img.png', icon_size=(40, 40))  # customized icon
folium.Marker(location=[10.799134430915721, 76.81813182028293], tooltip="<strong>Taste of Malabar</strong>",
              popup=popup1, icon=ricon).add_to(map)  # for displaying everything in the given icon


# for location 2: Ahalia foodball ground
picture2 = base64.b64encode(open("./ahaliafb.jpg", 'rb').read()).decode()
iframe2 = IFrame(html(picture2), width=327+20, height=218+20)
popup2 = folium.Popup(iframe2, max_width=640)
ricon2 = folium.features.CustomIcon('football.png', icon_size=(40, 40))
folium.Marker(location=[10.802291523435375, 76.81926446770233],
              tooltip="<strong>Ahalia Football Ground</strong>",
              popup=popup2, icon=ricon2).add_to(map)


# for location 3: Sculpture Park
picture3 = base64.b64encode(open("./sculp.jpg", 'rb').read()).decode()
iframe3 = IFrame(html(picture3), width=327+20, height=372+20)
popup3 = folium.Popup(iframe3, max_width=650)
ricon3 = folium.features.CustomIcon('stone.png', icon_size=(40, 40))
folium.Marker(location=[10.795959805319832, 76.82282023370011],
              tooltip="<strong>Ahalia Sculpture Park</strong>",
              popup=popup3, icon=ricon3).add_to(map)

# for loacation 4 : Cafe Coffee Day
picture4 = base64.b64encode(open("./cdc.jpg", 'rb').read()).decode()
iframe4 = IFrame(html(picture4), width=327+20, height=202+20)
popup4 = folium.Popup(iframe4, max_width=650)
ricon4 = folium.features.CustomIcon('img.png', icon_size=(40, 40))
folium.Marker(location=[10.800102523261407, 76.81888433684003],
              tooltip="<strong>Cafe Coffee Day</strong>",
              popup=popup4, icon=ricon4).add_to(map)

# for location 5: Ahalia food point
picture5 = base64.b64encode(open("./afp1.jpg", 'rb').read()).decode()
iframe5 = IFrame(html(picture5), width=327+20, height=242+20)
popup5 = folium.Popup(iframe5, max_width=640)
ricon5 = folium.features.CustomIcon('img.png', icon_size=(40, 40))
folium.Marker(location=[10.792262269988168, 76.82803937041948],
              tooltip="<strong>Ahalia Food Point</strong>",
              popup=popup5, icon=ricon5).add_to(map)

# for location 6: Ahalia Home Centre
picture6 = base64.b64encode(open("./hc.jpg", 'rb').read()).decode()
iframe6 = IFrame(html(picture6), width=327+20, height=187+20)
popup6 = folium.Popup(iframe6, max_width=640)
ricon6 = folium.features.CustomIcon('shop.png', icon_size=(60, 60))
folium.Marker(location=[10.792340364052299, 76.82816306640642],
              tooltip="<strong>Ahalia Home Centre</strong>",
              popup=popup6, icon=ricon6).add_to(map)

# for location 7: Ahalia Diabetic Hospital
picture7 = base64.b64encode(open("./adh.jpg", 'rb').read()).decode()
iframe7 = IFrame(html(picture7), width=327+20, height=225+20)
popup7 = folium.Popup(iframe7, max_width=640)
ricon7 = folium.features.CustomIcon('hosp.png', icon_size=(40, 40))
folium.Marker(location=[10.792077430340598, 76.82749318189833],
              tooltip="<strong>Ahalia Diabetic Hospital</strong>",
              popup=popup7, icon=ricon7).add_to(map)

# for location 8: Ahalia Ayurveda Hospital
picture8 = base64.b64encode(open("./ayur.jpg", 'rb').read()).decode()
iframe8 = IFrame(html(picture8), width=327+20, height=170+20)
popup8 = folium.Popup(iframe8, max_width=640)
ricon8 = folium.features.CustomIcon('hosp.png', icon_size=(40, 40))
folium.Marker(location=[10.791929710674356, 76.82899214327897],
              tooltip="<strong>Ahalia Ayurveda Hospital</strong>",
              popup=popup8, icon=ricon8).add_to(map)

# for location 9: Academic Block
picture_ab = base64.b64encode(open('./acad.jpg', 'rb').read()).decode()
iframe_ab = IFrame(html(picture_ab), width=327+20, height=245+20)
popup_ab = folium.Popup(iframe_ab, max_width=650)
ricon_ab = folium.features.CustomIcon('lib.png', icon_size=(40, 60))
folium.Marker(location=[10.8017955754564, 76.81849606364607],
              tooltip="<strong>Academic Block</strong>",
              popup=popup_ab, icon=ricon_ab).add_to(map)

# for location 10: Hostel 1
picture_h1 = base64.b64encode(open("./h1.jpg", 'rb').read()).decode()
iframe_h1 = IFrame(html(picture_h1), width=327+20, height=245+20)
popup_h1 = folium.Popup(iframe_h1, max_width=650)
ricon_h1 = folium.features.CustomIcon('home.png', icon_size=(60, 60))
folium.Marker(location=[10.799205621030923, 76.82223021773736],
              tooltip="<strong>Hostel 1</strong>",
              popup=popup_h1, icon=ricon_h1).add_to(map)

# for location 11: Hostel 2
picture_h2 = base64.b64encode(open('./h2.jpg', 'rb').read()).decode()
iframe_h2 = IFrame(html(picture_h2), width=327+20, height=245+20)
popup_h2 = folium.Popup(iframe_h2, max_width=650)
ricon_h2 = folium.features.CustomIcon('home.png', icon_size=(60, 60))
folium.Marker(location=[10.799550455187008, 76.8222669062808],
              tooltip="<strong>Hostel 2</strong>",
              popup=popup_h2, icon=ricon_h2).add_to(map)

# for location 12: Hostel 3
picture_h3 = base64.b64encode(open("./h3.jpg", 'rb').read()).decode()
iframe_h3 = IFrame(html(picture_h3), width=327+20, height=245+20)
popup_h3 = folium.Popup(iframe_h3, max_width=650)
ricon = folium.features.CustomIcon('home.png', icon_size=(60, 60))
folium.Marker(location=[10.797984370712905, 76.81832584827522],
              tooltip="<strong>Hostel 3</strong>",
              popup=popup_h3, icon=ricon).add_to(map)

# for location 13: Lake
picture_l = base64.b64encode(open("./lake.jpg", 'rb').read()).decode()
iframe_l = IFrame(html(picture_l), width=327+20, height=273+20)
popup_l = folium.Popup(iframe_l, max_width=650)
ricon_l = folium.features.CustomIcon('la.png', icon_size=(60, 60))
folium.Marker(location=[10.794969103780806, 76.82528481763399],
              tooltip="<strong>Lake park</strong>",
              popup=popup_l, icon=ricon_l).add_to(map)

# for location 14: Manju's Canteen
picture_man = base64.b64encode(open('manju.jpg', 'rb').read()).decode()
iframe_man = IFrame(html(picture_man), width=327+20, height=245+20)
popup_man = folium.Popup(iframe_man, max_width=650)
ricon_man = folium.features.CustomIcon('shop.png', icon_size=(60, 60))
folium.Marker(location=[10.801940636611368, 76.81835829549671],
              tooltip="<strong>Manju's Canteen</strong>",
              popup=popup_man, icon=ricon_man).add_to(map)

# for location 15: Mess
picture_mess = base64.b64encode(open('./mess.jpg', 'rb').read()).decode()
iframe_mess = IFrame(html(picture_mess), width=327+20, height=245+20)
popup_mess = folium.Popup(iframe_mess, max_width=650)
ricon_mess = folium.features.CustomIcon('img.png', icon_size=(40, 40))
folium.Marker(location=[10.799290457287118, 76.82241465360843],
              tooltip="<strong>Mess</strong>",
              popup=popup_mess, icon=ricon_mess).add_to(map)

# for location 16: Pharmacy Block
picture_ph = base64.b64encode(open('pharm.jpg', 'rb').read()).decode()
iframe_ph = IFrame(html(picture_ph), width=325+20, height=277+20)
popup_ph = folium.Popup(iframe_ph, max_width=650)
ricon_ph = folium.features.CustomIcon('lib.png', icon_size=(40, 60))
folium.Marker(location=[10.800699183782722, 76.81830260137629],
              tooltip="<strong>Pharmacy Block</strong>",
              popup=popup_ph, icon=ricon_ph).add_to(map)

# for location 17: Ahalia eye hospital
picture_aeh = base64.b64encode(open('aeh.jpg', 'rb').read()).decode()
iframe_aeh = IFrame(html(picture_aeh), width=327+20, height=208+20)
popup_aeh = folium.Popup(iframe_aeh, max_width=640)
ricon_aeh = folium.features.CustomIcon('hosp.png', icon_size=(40, 40))
folium.Marker(location=[10.794002645395077, 76.82705190698024],
              tooltip="<strong>Ahalia Eye Hospital</strong>",
              popup=popup_aeh, icon=ricon_aeh).add_to(map)

# for location 18: Canara Bank ATM
picture_ac = base64.b64encode(open('canara.jpg', 'rb').read()).decode()
iframe_ac = IFrame(html(picture_ac), width=327+20, height=437+20)
popup_ac = folium.Popup(iframe_ac, max_width=640)
ricon_ac = folium.features.CustomIcon('bank.png', icon_size=(40, 40))
folium.Marker(location=[10.800427387710556, 76.81835704549528],
              tooltip="<strong>Canara Bank ATM</strong>",
              popup=popup_ac, icon=ricon_ac).add_to(map)

# for location 19: Basket Ball court
picture_bk = base64.b64encode(open('basketball.jpg', 'rb').read()).decode()
iframe_bk = IFrame(html(picture_bk), width=327+20, height=245+20)
popup_bk = folium.Popup(iframe_bk, max_width=640)
ricon_bk = folium.features.CustomIcon('bb.png', icon_size=(40, 40))
folium.Marker(location=[10.802793275868506, 76.81854055985796],
              tooltip="<strong>Basketball Court</strong>",
              popup=popup_bk, icon=ricon_bk).add_to(map)

# for location 20: Staff Quaters
picture_st = base64.b64encode(open('staff.jpg', 'rb').read()).decode()  # change
iframe_st = IFrame(html(picture_st), width=327+20, height=245+20)
popup_st = folium.Popup(iframe_st, max_width=650)
ricon_st = folium.features.CustomIcon('home.png', icon_size=(60, 60))
folium.Marker(location=[10.797483655650366, 76.81746333689723],
              tooltip="<strong>Staff Quaters</strong>",
              popup=popup_st, icon=ricon_st).add_to(map)

# for location 21: Statue
picture_stat = base64.b64encode(
    open("statue.jpg", 'rb').read()).decode()  # change
iframe_stat = IFrame(html(picture_stat), width=327+20, height=440+20)
popup_stat = folium.Popup(iframe_stat, max_width=640)
ricon_stat = folium.features.CustomIcon('stone.png', icon_size=(40, 40))
folium.Marker(location=[10.79439732616303, 76.82345431105006],
              tooltip="<strong>Ahalia Statue</strong>",
              popup=popup_stat, icon=ricon_stat).add_to(map)

# for location 22: Volley Ball
picture_vb = base64.b64encode(open('volleyball.jpg', 'rb').read()).decode()
iframe_vb = IFrame(html(picture_vb), width=327+20, height=245+20)
popup_vb = folium.Popup(iframe_vb, max_width=640)
ricon_vb = folium.features.CustomIcon('vb.png', icon_size=(40, 38))
folium.Marker(location=[10.799264150220212, 76.82192429390716],
              tooltip="<strong>Ahalia Volleyball Ground</strong>",
              popup=popup_vb, icon=ricon_vb).add_to(map)

# for location 23: MBA block
picture_mba = base64.b64encode(open('mba.jpg', 'rb').read()).decode()
iframe_mba = IFrame(html(picture_mba), width=327+20, height=245+20)
popup_mba = folium.Popup(iframe_mba, max_width=650)
ricon_mba = folium.features.CustomIcon('lib.png', icon_size=(40, 60))
folium.Marker(location=[10.799334989848212, 76.82103835492995],
              tooltip="<strong>MBA Block</strong>",
              popup=popup_mba, icon=ricon_mba).add_to(map)

map.save("map.html")  # saving the file as map.html
