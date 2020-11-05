#kovur 14.5021° N, 79.9853° E
import folium
m1=folium.Map(location=(14.5021,79.9853),zoom_start=15)
fg=folium.FeatureGroup(name='mymap')
fg.add_child(folium.Marker(location=(14.5021,79.9853),icon=folium.Icon()))
m1.add_child(fg)
m1.save('kovur.html')
