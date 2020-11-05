import csv
import folium
m1=folium.Map(location=(20.5937, 78.9629),zoom_start=4)
fg = folium.FeatureGroup(name='india captials')
with open('captials.csv')as csvfile:
    next(csvfile)
    readcsv=csv.reader(csvfile,delimiter=',')
    for row in readcsv:
       # print(row[1])
        x = row[0]
        y=row[1]
        z=row[2]
        u=row[3]
        fg.add_child(folium.Marker(location=(float(y), float(z)),popup=str(x),icon=folium.Icon(color=str(u))))
m1.add_child(fg)
m1.save('allcaptials.html')
