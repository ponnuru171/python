import pandas as pd
weather_data = [('1/1/2017','Nellore', 32, 6, 'Rain'),
                ('1/2/2017', 'Ongle',35, 7, 'Sunny'),
                ('1/3/2017', 'Nellore',28, 2, 'Snow'),
                ('1/4/2017', 'Vizag',24, 7, 'Snow'),
                ('1/5/2017', 'Srikakulam',32, 4, 'Rain'),
                ('1/6/2017', 'Kadapa',31, 2, 'Sunny')
               ]
df = pd.DataFrame(weather_data, columns=['day', 'city','temperature', 'windspeed', 'event'])
print(df)
grp=df.groupby("city")
print(grp.get_group('Nellore'))
