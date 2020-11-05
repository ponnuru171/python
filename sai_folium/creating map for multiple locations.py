import folium
m1=folium.Map(location=(15.9129, 79.7400),zoom_start=6)
fg=folium.FeatureGroup(name='mymap')
fg.add_child(folium.Marker(location=(14.5021,79.9853),popup="kovur",icon=folium.Icon(color="green")))
fg.add_child(folium.Marker(location=(14.4426, 79.9865),popup="nellore",icon=folium.Icon(color="red")))
fg.add_child(folium.Marker(location=(17.3850, 78.4867),popup="hyderbad",icon=folium.Icon(color="blue")))
fg.add_child(folium.Marker(location=(17.6868, 83.2185),icon=folium.Icon()))
m1.add_child(fg)
m1.save('nellore.html')
